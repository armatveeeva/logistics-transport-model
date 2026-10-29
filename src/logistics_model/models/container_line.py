from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.port import Port


class ContainerLine(Base):
    __tablename__ = "container_line"

    id: Mapped[int] = mapped_column(primary_key=True)
    port_id: Mapped[int] = mapped_column(ForeignKey("port.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    agent: Mapped[str | None] = mapped_column(String(200))

    port: Mapped["Port"] = relationship(back_populates="container_lines")
