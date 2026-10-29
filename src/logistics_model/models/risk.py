from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from logistics_model.database import Base

if TYPE_CHECKING:
    from logistics_model.models.incident import Incident


class Risk(Base):
    __tablename__ = "risk"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incident.id"))
    name = Column(String, nullable=False)
    weight = Column(Integer)
    cost = Column(Float)
    currency = Column(String)

    incident: Mapped["Incident | None"] = relationship(back_populates="risks")
