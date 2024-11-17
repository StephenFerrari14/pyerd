from pydantic import BaseModel


class BaseDonut(BaseModel):
    id: int


class Donut(BaseDonut):
    name: str


class Glazed(Donut):
    glazed: bool = True
