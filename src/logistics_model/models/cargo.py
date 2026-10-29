from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from logistics_model.database import Base


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Float)
    currency = Column(String)

    # Связи
    incidents = relationship("Incident", back_populates="cargo")
