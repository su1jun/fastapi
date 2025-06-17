from typing import Union, List
from fastapi import FastAPI, Query

app = FastAPI()

""" @app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """

# add regex pattern
""" @app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """

# default value
""" @app.get("/items/")
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """

# required query parameter
""" @app.get("/items/")
async def read_items(q: str = Query(min_length=3)): # from typing_extensions import Annotated; (q: Annotated[str, Query(min_length=3)])
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """

# multiple query parameters
@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)): # (q: list = Query(default=[]))
    query_items = {"q": q}
    return query_items

# add metadata to query parameter
@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")): # http://127.0.0.1:8000/items/?item-query=foobaritems <- alias
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results