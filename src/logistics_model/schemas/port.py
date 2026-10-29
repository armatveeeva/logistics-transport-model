from pydantic import BaseModel, Field


class PortIn(BaseModel):
    name: str = Field(min_length=1, max_length=100, description="Название порта")
    basin_id: int = Field(gt=0, description="ID бассейна")
    container_turnover: float | None = Field(default=None, ge=0)
