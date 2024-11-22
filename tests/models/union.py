import typing
from pydantic import BaseModel

class Jack(BaseModel):
  colors: typing.Union[str, int]
  states: dict | list
  raised: bool | None