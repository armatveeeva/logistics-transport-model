from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import Mapped, relationship

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.incident import Incident


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Float)
    currency = Column(String)

    incidents: Mapped[list["Incident"]] = relationship(back_populates="cargo")
