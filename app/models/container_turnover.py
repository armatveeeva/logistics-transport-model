from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class ContainerTurnover(Base):
    __tablename__ = "container_turnover"

    id = Column(Integer, primary_key=True, index=True)
    port_id = Column(Integer, ForeignKey("port.id"))
    cabotage_loaded = Column(Float, default=0)
    cabotage_empty = Column(Float, default=0)
    import_volume = Column(Float, default=0)
    export_volume = Column(Float, default=0)
    export_loaded = Column(Float, default=0)
    export_empty = Column(Float, default=0)
    transit = Column(Float, default=0)
    teu = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

    # Связи
    port = relationship("Port", back_populates="container_turnovers")