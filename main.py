from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    # model_config = {"extra": "forbid"} # forbid extra fields
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers

# {
#     "detail": [
#         {
#             "type": "extra_forbidden",
#             "loc": ["header", "tool"],
#             "msg": "Extra inputs are not permitted",
#             "input": "plumbus",
#         }
#     ]
# }
