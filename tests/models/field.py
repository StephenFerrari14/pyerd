from pydantic import BaseModel, Field

class Roast(BaseModel):
  name: str = Field(min_length=1) 
  price: int