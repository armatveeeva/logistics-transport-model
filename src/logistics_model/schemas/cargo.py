from pydantic import BaseModel, Field


class CargoIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    cargo_type: str | None = Field(default=None, max_length=50)
    cost: float | None = Field(default=None, ge=0)
    currency: str | None = Field(default=None, max_length=3)
