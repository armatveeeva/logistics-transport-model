from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Incident(Base):
    __tablename__ = "incident"

    id = Column(Integer, primary_key=True, index=True)
    cargo_id = Column(Integer, ForeignKey("cargo.id"), nullable=True)
    operator_id = Column(Integer, ForeignKey("operator.id"), nullable=True)
    port_id = Column(Integer, ForeignKey("port.id"), nullable=True)
    container_line_id = Column(Integer, ForeignKey("container_line.id"), nullable=True)
    basin_id = Column(Integer, ForeignKey("basin.id"), nullable=True)
    type = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    description = Column(String)
    economic_damage = Column(Float)
    economic_damage_currency = Column(String)

    # Связи
    cargo = relationship("Cargo", back_populates="incidents")
    operator = relationship("Operator", back_populates="incidents")
    port = relationship("Port", back_populates="incidents")
    container_line = relationship("ContainerLine", back_populates="incidents")
    basin = relationship("Basin", back_populates="incidents")
    risks = relationship("Risk", back_populates="incident")