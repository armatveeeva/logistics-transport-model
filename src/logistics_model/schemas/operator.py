from pydantic import BaseModel, Field


class OperatorIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    port_id: int = Field(gt=0)
    inn: str | None = Field(default=None, min_length=10, max_length=12)
    address: str | None = Field(default=None, max_length=300)
