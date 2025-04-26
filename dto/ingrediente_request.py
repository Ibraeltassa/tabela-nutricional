from pydantic import BaseModel
from typing import List

class IngredientesRequestDTO(BaseModel):
    nomes: List[str]
