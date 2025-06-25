from typing import List, Optional
from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
