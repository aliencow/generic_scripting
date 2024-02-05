
## FastAPI paths

Path is the first parameter in decorator function 
@app.get("path")

It can be either a simple route like "/","/users/me" or include some parameter (inside brackets) like "/users/{item_id}". The value of the path parameter item_id will be passed to your function as the argument item_id.
``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
````

You must consider that:

1. Path operations are evaluated in order
2. you cannot redefine a path operation (repeat get f.e.)
3. If you want the possible valid path parameter values to be predefined, you can use a standard Python Enum

``` python
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

### en el navegador se pondría así http://127.0.0.1:8000/bands/gemodels/mi_modelo 
# suponiendo que el model_name fuera mi_modelo

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

## Query parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

```

The query is the set of key-value pairs that go after the `?` in a URL, separated by `&` characters.

For example, in the URL:


`http://127.0.0.1:8000/items/?skip=0&limit=10`

...the query parameters are:

skip: with a value of 0
limit: with a value of 10
As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

All the same process that applied for path parameters also applies for query parameters:

* Editor support (obviously)
* Data "parsing"
* Data validation
* Automatic documentation