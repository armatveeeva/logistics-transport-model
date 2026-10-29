from datetime import date

from pydantic import BaseModel, Field


class ContainerTurnoverIn(BaseModel):
    port_id: int = Field(gt=0)
    date: date
    cabotage_loaded: float | None = Field(default=None, ge=0)
    cabotage_empty: float | None = Field(default=None, ge=0)
    import_volume: float | None = Field(default=None, ge=0)
    export_volume: float | None = Field(default=None, ge=0)
    export_loaded: float | None = Field(default=None, ge=0)
    export_empty: float | None = Field(default=None, ge=0)
    transit: float | None = Field(default=None, ge=0)
    teu: float | None = Field(default=None, ge=0)
