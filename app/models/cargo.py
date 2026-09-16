from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Float)
    currency = Column(String)

    # Связи
    incidents = relationship("Incident", back_populates="cargo")