import logging
from datetime import date, datetime
from pathlib import Path

import pandas as pd
from pydantic import ValidationError
from sqlalchemy.orm import Session

from logistics_model.database import Base
from logistics_model.repositories.base import BaseRepository
from logistics_model.schemas import (
    BasinIn,
    CargoIn,
    ContainerLineIn,
    ContainerTurnoverIn,
    IncidentIn,
    OperatorIn,
    PortIn,
    RiskIn,
    ServiceTypeIn,
)

logger = logging.getLogger(__name__)

TABLE_REGISTRY = {
    "basin": (BasinIn, None),
    "cargo": (CargoIn, None),
    "service_type": (ServiceTypeIn, None),
    "port": (PortIn, None),
    "container_line": (ContainerLineIn, None),
    "container_turnover": (ContainerTurnoverIn, None),
    "operator": (OperatorIn, None),
    "incident": (IncidentIn, None),
    "risk": (RiskIn, None),
}


def _coerce_dates(row: dict, schema_cls: type) -> dict:
    """Преобразует строки в datetime.date там, где схема ожидает date."""
    hints = schema_cls.model_fields
    for field_name, field_info in hints.items():
        if field_name not in row or row[field_name] is None:
            continue
        annotation = field_info.annotation
        if annotation is date and isinstance(row[field_name], (str, datetime)):
            try:
                row[field_name] = pd.to_datetime(row[field_name]).date()
            except (ValueError, TypeError):
                row[field_name] = None
    return row


def load_workbook(session: Session, excel_path: str) -> None:
    """Загружает Excel в БД с Pydantic-валидацией каждой строки."""
    path = Path(excel_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не найден")

    logger.info("Чтение файла %s...", path.name)
    sheets = pd.read_excel(path, sheet_name=None)
    tables = Base.metadata.sorted_tables

    for table in tables:
        if table.name in TABLE_REGISTRY:
            schema_cls, _ = TABLE_REGISTRY[table.name]
            TABLE_REGISTRY[table.name] = (schema_cls, table)

    with session.begin():
        for table in reversed(tables):
            session.execute(table.delete())

        for table in tables:
            if table.name not in TABLE_REGISTRY:
                logger.warning("Таблица '%s' не имеет Pydantic-схемы, пропускаем", table.name)
                continue

            schema_cls, _ = TABLE_REGISTRY[table.name]
            df = sheets.get(table.name)
            if df is None or df.empty:
                logger.warning("Лист '%s' пуст или отсутствует", table.name)
                continue

            valid: list = []
            rejected = 0
            for index, row in df.iterrows():
                clean = {k: v for k, v in row.to_dict().items() if pd.notna(v)}
                clean = _coerce_dates(clean, schema_cls)
                try:
                    validated = schema_cls(**clean)
                    valid.append(validated)
                except ValidationError as e:
                    rejected += 1
                    if rejected <= 3:  # логируем первые 3 ошибки на таблицу
                        logger.warning(
                            "Строка %d в '%s' отклонена: %s", index, table.name, e.errors()[0]
                        )

            if valid:
                repo = BaseRepository(session, table, schema_cls)
                count = repo.insert_many(valid)
                logger.info(
                    "Загружено в '%s': %d записей (отклонено: %d)", table.name, count, rejected
                )
            elif rejected:
                logger.error("Все %d записей в '%s' отклонены валидацией", rejected, table.name)

    logger.info("Загрузка данных завершена")
