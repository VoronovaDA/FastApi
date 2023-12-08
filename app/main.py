""" main """
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings

app = FastAPI()


class Item(BaseModel):
    """ class item """
    name: str
    price: float


@app.get(settings.MAIN_URL)
def read_root():
    """ get endpoint """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """ get item id """
    return {"item_id": item_id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """ update item """
    return {"item_name": item.name, "item_id": item_id}
