from pydantic import BaseModel, Field


class RiskIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    incident_id: int = Field(gt=0)
    weight: int | None = Field(default=None, ge=0)
    currency: str | None = Field(default=None, max_length=3)
