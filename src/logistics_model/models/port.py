from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.basin import Basin
    from logistics_model.models.container_line import ContainerLine
    from logistics_model.models.container_turnover import ContainerTurnover
    from logistics_model.models.incident import Incident
    from logistics_model.models.operator import Operator


class Port(Base):
    __tablename__ = "port"

    id: Mapped[int] = mapped_column(primary_key=True)
    basin_id: Mapped[int] = mapped_column(ForeignKey("basin.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    container_turnover: Mapped[float | None] = mapped_column(Float)
    berth_count: Mapped[int | None] = mapped_column()
    throughput_capacity: Mapped[float | None] = mapped_column(Float)

    basin: Mapped["Basin"] = relationship(back_populates="ports")
    container_lines: Mapped[list["ContainerLine"]] = relationship(back_populates="port")
    container_turnovers: Mapped[list["ContainerTurnover"]] = relationship(back_populates="port")
    operators: Mapped[list["Operator"]] = relationship(back_populates="port")
    incidents: Mapped[list["Incident"]] = relationship(back_populates="port")
