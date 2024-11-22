from typing import Union
from pydantic import BaseModel


class BaseDonut(BaseModel):
    id: int


class Donut(BaseDonut):
    name: str


class Glazed(Donut):
    glazed: bool = True
    sprinkles: str | None = None
    topping: Union[int, str]
