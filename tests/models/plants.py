from pydantic import BaseModel, ConfigDict

from tests.models.common import User


class BasePlant(BaseModel):
    id: int
    type: str


class HousePlant(BasePlant):
    house_name: str
    owner: User
    
    model_config = ConfigDict(from_attributes=False)

