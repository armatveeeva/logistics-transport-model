from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import Table
from sqlalchemy.orm import Session

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    """Универсальный репозиторий для валидированных Pydantic-моделей."""

    def __init__(self, session: Session, table: Table, schema_cls: type[T]):
        self.session = session
        self.table = table
        self.schema_cls = schema_cls

    def insert_many(self, items: list[T]) -> int:
        records = [item.model_dump() for item in items]
        if not records:
            return 0
        result = self.session.execute(self.table.insert(), records)
        return int(result.rowcount) if result.rowcount else 0  # type: ignore
