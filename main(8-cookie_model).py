from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    # model_config = {"extra": "forbid"} # forbid extra fields
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies

# output
#{
#    "detail": [
#        {
#            "type": "extra_forbidden",
#            "loc": ["cookie", "santa_tracker"],
#            "msg": "Extra inputs are not permitted",
#            "input": "good-list-please",
#        }
#    ]
#}
