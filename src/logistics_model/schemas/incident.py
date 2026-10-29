from datetime import date

from pydantic import BaseModel, Field


class IncidentIn(BaseModel):
    type: str = Field(min_length=1, max_length=100)
    date: date
    description: str | None = Field(default=None, max_length=2000)
    port_id: int | None = Field(default=None, gt=0)
    operator_id: int | None = Field(default=None, gt=0)
    cargo_id: int | None = Field(default=None, gt=0)
    container_line_id: int | None = Field(default=None, gt=0)
    basin_id: int | None = Field(default=None, gt=0)
    economic_damage_currency: str | None = Field(default=None, max_length=3)
