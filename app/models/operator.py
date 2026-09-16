from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Operator(Base):
    __tablename__ = "operator"

    id = Column(Integer, primary_key=True, index=True)
    port_id = Column(Integer, ForeignKey("port.id"))
    name = Column(String, nullable=False)
    transhipment_volume = Column(Float)
    inn = Column(String)
    address = Column(String)
    throughput_capacity = Column(Float)

    # Связи
    port = relationship("Port", back_populates="operators")
    services = relationship("OperatorService", back_populates="operator")
    incidents = relationship("Incident", back_populates="operator")