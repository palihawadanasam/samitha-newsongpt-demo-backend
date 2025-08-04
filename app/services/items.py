from datetime import datetime
from app.models.schemas import ItemCreate, ItemResponse

class ItemService:
    def __init__(self):
        self.items = []
        self.next_id = 1

    def create_item(self, item: ItemCreate) -> ItemResponse:
        new_item = ItemResponse(
            id=self.next_id,
            **item.model_dump(),
            created_at=datetime.now()
        )
        self.items.append(new_item)
        self.next_id += 1
        return new_item