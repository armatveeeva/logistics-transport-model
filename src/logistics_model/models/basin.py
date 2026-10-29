from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.port import Port


class Basin(Base):
    __tablename__ = "basin"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    ports: Mapped[list["Port"]] = relationship(back_populates="basin")
