from sqlalchemy import Column, Integer, String
from app.database import Base

class Basin(Base):
    __tablename__ = "basin"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)