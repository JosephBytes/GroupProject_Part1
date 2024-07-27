import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf
from sqlalchemy.orm import Session

from .controllers import account
from .controllers import menu_item
from .controllers import order_details
from .controllers import account
from .controllers import payment
from .controllers import promotions
from .controllers import recipes
from .controllers import resources

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#not sure if this is the right implementation at all, but wanted to give it a go

#account
@app.post("/account/", response_model=account.Order, tags=["account"])
def create_order(order: account.accountCreate, db: Session):
    return order.create(db=db, account=account)


@app.get("/account/", response_model=list[account.Order], tags=["account"])
def read_account(db: Session):
    return account.read_all(db)


@app.get("/account/{order_id}", response_model=account.Order, tags=["account"])
def read_one_order(order_id: int, db: Session):
    order = account.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/account/{order_id}", response_model=account.Order, tags=["account"])
def update_one_order(order_id: int, order: account.OrderUpdate, db: Session):
    order_db = account.read_one(db, item_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.update(db=db, order=order, item_id=order_id)


@app.delete("/account/{order_id}", tags=["account"])
def delete_one_order(order_id: int, db: Session):
    order = account.read_one(db, item_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.delete(db=db, item_id=menu_item)

#resources
@app.get("/resources/", response_model=list[resources.Resource], tags=["Resource"])
def read_resources(db: Session):
    return resources.read_all(db)


@app.get("/resources/{resources_id}", response_model=resources.Resource, tags=["Resource"])
def read_one_resource(resources_id: int, db: Session):
    resource = resources.read_one(db, item_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resources_id}", response_model=resources.Resource, tags=["Resource"])
def update_one_resource(resources_id: int, resource: resources.ResourceUpdate, db: Session):
    resource_db = resource.read_one(db, item_id=resources_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.update(db=db, resource=resource, item_id=resources_id)


@app.delete("/resources/{resources_id}", tags=["Resource"])
def delete_one_resource(resources_id: int, db: Session):
    resource = resources.read_one(db, item_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.delete(db=db, resources_id=resources_id)

#recipes
@app.post("/recipes/", response_model=recipes.Recipe, tags=["Recipe"])
def create_recipe(recipe: recipes.RecipeCreate, db: Session ):
    return recipe.create(db=db, recipe=recipe)


@app.get("/recipes/", response_model=list[recipes.Recipe], tags=["Recipe"])
def read_recipes(db: Session):
    return recipes.read_all(db)


@app.get("/recipes/{recipes_id}", response_model=recipes.Recipe, tags=["Recipe"])
def read_one_recipe(recipes_id: int, db: Session):
    recipe = recipes.read_one(db, item_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipes/{recipes_id}", response_model=recipes.Recipe, tags=["Recipe"])
def update_one_recipe(recipes_id: int, recipe: recipes.RecipeUpdate, db: Session):
    recipe_db = recipe.read_one(db, item_id=recipes_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.update(db=db, recipe=recipe, item_id=recipes_id)


@app.delete("/recipes/{recipes_id}", tags=["Recipe"])
def delete_one_recipe(recipes_id: int, db: Session):
    recipe = recipes.read_one(db, item_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.delete(db=db, item_id=recipes_id)

#order details
@app.post("/order_details/", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def create_order_detail(order_detail: order_details.OrderDetailCreate, db: Session):
    return order_detail.create(db=db, item_id=order_detail)


@app.get("/order_details/", response_model=list[order_details.OrderDetail], tags=["OrderDetail"])
def read_order_details(db: Session):
    return order_details.read_all(db)


@app.get("/order_details/{order_details_id}", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def read_one_order_detail(order_details_id: int, db: Session):
    order_detail = order_details.read_one(db, item_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail


@app.put("/order_details/{order_details_id}", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def update_one_order_detail(order_details_id: int, order_detail: order_details.OrderDetailUpdate,
                            db: Session):
    order_detail_db = order_detail.read_one(db, order_details_id=order_details_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.update(db=db, order_detail=order_detail, order_details_id=order_details_id)


@app.delete("/order_details/{order_details_id}", tags=["OrderDetail"])
def delete_one_order_detail(order_details_id: int, db: Session):
    order_detail = order_details.read_one(db, item_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.delete(db=db, order_details_id=order_details_id)

#accounts
@app.get("/account/", response_model=list[account.Account], tags=["account"])
def read_account(db: Session):
    return account.read_all(db)


@app.get("/account/{order_id}", response_model=account.Account, tags=["account"])
def read_one_account(account_id: int, db: Session):
    accounts = account.read_one(db, item_id=account_id)
    if accounts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return accounts


@app.put("/account/{account_id}", response_model=account.Account, tags=["account"])
def update_one_account(account_id: int, account: account.AccountUpdate, db: Session):
    account_db = account.read_one(db, item_id=account_id)
    if account_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.update(db=db, account=account, item_id=account_id)


@app.delete("/account/{account_id}", tags=["account"])
def delete_one_account(account_id: int, db: Session):
    accounts = account.read_one(db, item_id=account_id)
    if accounts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.delete(db=db, item_id=menu_item)

#payment


model_loader.index()
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
