import logging
from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Date, DateTime

from logistics_model.database import Base

logger = logging.getLogger(__name__)


def load_workbook(session: Session, excel_path: str) -> None:
    """Безопасно загружает данные из Excel в существующие таблицы БД с учетом типов."""
    path = Path(excel_path)
    if not path.exists():
        logger.error("Файл %s не найден", path)
        raise FileNotFoundError(f"Файл {path} не найден")

    logger.info("Чтение файла %s...", path.name)
    sheets = pd.read_excel(path, sheet_name=None)

    tables = Base.metadata.sorted_tables

    with session.begin():
        logger.info("Очистка существующих данных...")
        for table in reversed(tables):
            session.execute(table.delete())

        for table in tables:
            df = sheets.get(table.name)
            if df is None or df.empty:
                logger.warning("Лист '%s' пуст или отсутствует в Excel", table.name)
                continue

            for col in df.columns:
                column_obj = table.c.get(col)
                if column_obj is not None and isinstance(column_obj.type, Date | DateTime):
                    df[col] = pd.to_datetime(df[col], errors="coerce")

            rows = [
                {str(k): v for k, v in row.items()}
                for row in df.astype(object).where(pd.notna(df), None).to_dict("records")
            ]

            session.execute(table.insert(), rows)
            logger.info("Загружено в таблицу '%s': %d записей", table.name, len(rows))

    logger.info("Загрузка данных успешно завершена!")
