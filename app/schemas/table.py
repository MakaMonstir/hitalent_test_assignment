from pydantic import BaseModel, ConfigDict


class TableBase(BaseModel):
    name: str
    seats: int
    location: str | None = None


class TableCreate(TableBase):
    pass


class TableOut(TableBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

