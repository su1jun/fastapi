from typing import Set, List, Union
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# standard list usage
# my_list: List[str]

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None # second example


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

