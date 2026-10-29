from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship  # <-- Добавьте Mapped сюда!

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.port import Port


class ContainerTurnover(Base):
    __tablename__ = "container_turnover"

    id: Mapped[int] = mapped_column(primary_key=True)
    port_id: Mapped[int] = mapped_column(ForeignKey("port.id"))
    date: Mapped[date] = mapped_column(Date)
    cabotage_loaded: Mapped[float | None] = mapped_column(Float)
    cabotage_empty: Mapped[float | None] = mapped_column(Float)
    import_volume: Mapped[float | None] = mapped_column(Float)
    export_volume: Mapped[float | None] = mapped_column(Float)
    export_loaded: Mapped[float | None] = mapped_column(Float)
    export_empty: Mapped[float | None] = mapped_column(Float)
    transit: Mapped[float | None] = mapped_column(Float)
    teu: Mapped[float | None] = mapped_column(Float)

    port: Mapped["Port"] = relationship(back_populates="container_turnovers")
