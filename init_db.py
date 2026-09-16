from app.database import Base, engine

from app.models import (
    Basin, Port, Operator, ServiceType, ContainerLine,
    ContainerTurnover, Cargo, Incident, Risk
)

def init_db():
    print("Начинается создание таблиц в базе данных...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы в logistics.db!")

if __name__ == "__main__":
    init_db()