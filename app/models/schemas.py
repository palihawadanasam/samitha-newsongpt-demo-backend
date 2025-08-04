from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str | None = None

class ItemCreate(ItemBase):
    price: float = Field(..., gt=0)

class ItemResponse(ItemBase):
    id: int
    price: float
    created_at: float