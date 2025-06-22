from typing import Set, List, Dict, Union
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

# deep recursive model declare
class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}

# deep recursive model
@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# list type in argument
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

# type type in argument
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

