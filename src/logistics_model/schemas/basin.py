from pydantic import BaseModel, Field


class BasinIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
