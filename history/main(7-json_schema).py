from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
  item_id: int,
  item: Annotated[
    Item,
    Body(
      examples=[
        {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
        {
            "name": "Bar",
            "price": "35.4",
        },
        {
            "name": "Baz",
            "price": "thirty five point four",
        },
      ],
    ),
  ],
):
    
  results = {"item_id": item_id, "item": item}
  return results