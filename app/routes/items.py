from fastapi import APIRouter, Depends, HTTPException
from app.services.items import ItemService
from app.models.schemas import ItemCreate, ItemResponse

router = APIRouter(tags=["Items"])

@router.post("/", response_model=ItemResponse)
async def create_item(
    item: ItemCreate, 
    service: ItemService = Depends(ItemService)
):
    try:
        return service.create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))