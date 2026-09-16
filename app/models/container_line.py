from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ContainerLine(Base):
    __tablename__ = "container_line"

    id = Column(Integer, primary_key=True, index=True)
    port_id = Column(Integer, ForeignKey("port.id"))
    name = Column(String, nullable=False)
    agent = Column(String)

    # Связи
    port = relationship("Port", back_populates="container_lines")
    incidents = relationship("Incident", back_populates="container_line")