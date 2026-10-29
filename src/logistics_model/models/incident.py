from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship  # <-- Проверьте наличие Mapped

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.cargo import Cargo
    from logistics_model.models.port import Port
    from logistics_model.models.risk import Risk


class Incident(Base):
    __tablename__ = "incident"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[date] = mapped_column(Date)
    description: Mapped[str | None] = mapped_column(String(2000))
    port_id: Mapped[int | None] = mapped_column(ForeignKey("port.id"))
    operator_id: Mapped[int | None] = mapped_column(ForeignKey("operator.id"))
    cargo_id: Mapped[int | None] = mapped_column(ForeignKey("cargo.id"))
    container_line_id: Mapped[int | None] = mapped_column(ForeignKey("container_line.id"))
    basin_id: Mapped[int | None] = mapped_column(ForeignKey("basin.id"))
    economic_damage_currency: Mapped[str | None] = mapped_column(String(3))
    port: Mapped["Port"] = relationship(back_populates="incidents")
    cargo: Mapped["Cargo | None"] = relationship(back_populates="incidents")
    risks: Mapped[list["Risk"]] = relationship(back_populates="incident")
