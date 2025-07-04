from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

""" class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None

  # reply data example
  model_config = {
      "json_schema_extra": {
          "examples": [
              {
                  "name": "Foo",
                  "description": "A very nice Item",
                  "price": 35.4,
                  "tax": 3.2,
              }
          ]
      }
  } """

# another example -> show reply data example 
class Item(BaseModel):
  name: str = Field(examples=["Foo"])
  description: str | None = Field(default=None, examples=["A very nice Item"])
  price: float = Field(examples=[35.4])
  tax: float | None = Field(default=None, examples=[3.2])

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
  results = {"item_id": item_id, "item": item}
  return results