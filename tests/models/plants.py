from pydantic import BaseModel

from tests.models.common import User


class BasePlant(BaseModel):
    id: int
    type: str


class HousePlant(BasePlant):
    house_name: str
    owner: User
