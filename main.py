from fastapi import FastAPI
from pydantic import BaseModel

# Pydantic datamodel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

""" @app.post("/items/")
async def create_item(item: Item):
    return item

# parameter description
@app.post("/items/")
async def create_item(item: Item):
    return item
 """
# use pydantic model to modify the request body
## request body
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

## request body, route parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

## request body, route parameters, query parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
