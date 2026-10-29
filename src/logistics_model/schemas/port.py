from pydantic import BaseModel, Field


class PortIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    basin_id: int = Field(gt=0)
    container_turnover: float | None = Field(default=None, ge=0)
    berth_count: int | None = Field(default=None, ge=0)
    throughput_capacity: float | None = Field(default=None, ge=0)
