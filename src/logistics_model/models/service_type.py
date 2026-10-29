from sqlalchemy import Column, Integer, String

from logistics_model.database import Base


class ServiceType(Base):
    __tablename__ = "service_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
