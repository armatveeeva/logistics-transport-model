from pydantic import BaseModel, Field


class ContainerLineIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    port_id: int = Field(gt=0)
    agent: str | None = Field(default=None, max_length=200)
