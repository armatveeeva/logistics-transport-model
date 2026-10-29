from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from logistics_model.database import Base


class Risk(Base):
    __tablename__ = "risk"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incident.id"))
    name = Column(String, nullable=False)
    weight = Column(Integer)
    cost = Column(Float)
    currency = Column(String)

    # Связи
    incident = relationship("Incident", back_populates="risks")
