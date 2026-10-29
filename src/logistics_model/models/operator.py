from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship  # <-- Проверьте наличие Mapped

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.port import Port


class Operator(Base):
    __tablename__ = "operator"

    id: Mapped[int] = mapped_column(primary_key=True)
    port_id: Mapped[int] = mapped_column(ForeignKey("port.id"))
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    inn: Mapped[str | None] = mapped_column(String(12))
    address: Mapped[str | None] = mapped_column(String(300))

    port: Mapped["Port"] = relationship(back_populates="operators")
