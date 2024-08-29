from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl 
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title='Description')
    price: float = Field(gt=0, title='Price')
    tax: float | None = None
    tags: list[str] = []
    image: Image | None = None

    model_config = {
        'json_schema_extra': [
            {
                    "name": "string",
                    "description": "string",
                    "price": 1,
                    "tax": 0,
                    "tags": [],
                    "image": {
                        "url": "https://example.com/image.png",
                        "name": "string"
                    }
            }
        ]
    }

class User(BaseModel):
    username: str
    fullname: str | None = None
    

@app.post("/items/")
async def create_item(item: Item):

    for tag in item.tags:
        print(tag)


    return item

# --------------------------------------------

# @app.post("/items/")
# async def create_item(item: Item):
#     return item.tax + item.price

# @app.put("/items/{item_id}")
# async def create_item(item_id : int, item: Item):
#     return {"item_id": item_id,**item.dict()}

# @app.put("/items/{item_id}")
# async def create_item(item_id : Annotated[int, Path(ge=1, le=1000)], 
#                       item: Item, 
#                       search: str| None = None):
#     if search:
#         return "Searched"
#     return {"item_id": item_id,**item.dict()}

# --------------------------------------------

# @app.put("/items/{item_id}")
# async def create_item(item_id : Annotated[int, Path(ge=1, le=1000)], 
#                       item: Item, 
#                       user: User,
#                       importance: Annotated[int, Body()]):
#     return {"item_id": item_id,**item.dict(), 'user': user, 'item': item, 'importance': importance}

# --------------------------------------------

# @app.post("/items/")
# async def create_item(item: Annotated[Item, Body(embed=True)]):
#     return item