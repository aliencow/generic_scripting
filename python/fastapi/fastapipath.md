
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


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

## How to avoid an authentication middleware to ask credentials on swagger ui route
https://github.com/tiangolo/fastapi/discussions/9827

## Super big fastAPI tutorial
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6b-linode-deploy-gunicorn-uvicorn-nginx/


jinja2templates
https://github.com/smartexpert/fastjinja2templates

## fastapi CRUD application
https://testdriven.io/blog/fastapi-mongo/

## Create a Authentication System Using FastApi and PostgreSql Login,Logout
https://medium.com/@chnarsimha986/fastapi-login-logout-changepassword-4c12e92d41e2
