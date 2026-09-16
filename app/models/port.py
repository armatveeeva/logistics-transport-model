from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Port(Base):
    __tablename__ = "port"

    id = Column(Integer, primary_key=True)
    basin_id = Column(Integer, ForeignKey("basin.id"))
    name = Column(String, nullable=False)
    container_turnover = Column(Float)
    berth_count = Column(Integer)
    throughput_capacity = Column(Float)

    basin = relationship("Basin")