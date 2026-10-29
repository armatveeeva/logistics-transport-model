import logging
import sys
from pathlib import Path

from logistics_model.config import settings
from logistics_model.database import SessionLocal
from logistics_model.services.loader import load_workbook

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL if hasattr(settings, "LOG_LEVEL") else "INFO"),
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    excel_path = Path("data/seed/export_logistics_db.xlsx")
    if not excel_path.exists():
        excel_path = Path("export_logistics_db.xlsx")

    if not excel_path.exists():
        logger.error("Не удалось найти файл export_logistics_db.xlsx")
        sys.exit(1)

    logger.info("Инициализация подключения к БД: %s", settings.DATABASE_URL)

    try:
        with SessionLocal() as session:
            load_workbook(session, str(excel_path))
        logger.info("Процесс завершен успешно.")
    except Exception as e:
        logger.error("Ошибка при загрузке данных: %s", e, exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
