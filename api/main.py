import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf
from .dependencies.database import engine, get_db
from sqlalchemy.orm import Session

from .controllers import orders
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

#orders
@app.post("/orders/", response_model=orders.Order, tags=["orders"])
def create_order(order: orders.OrderCreate, db: Session = Depends(get_db)):
    return order.create(db=db, order=order)


@app.get("/orders/", response_model=list[orders.Order], tags=["orders"])
def read_account(db: Session = Depends(get_db)):
    return account.read_all(db)


@app.get("/orders/{order_id}", response_model=orders.Order, tags=["orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db,  item_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=orders.Order, tags=["orders"])
def update_one_order(order_id: int, order: orders.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, item_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order.update(db=db, order=order,  item_id=order_id)


@app.delete("/orders/{order_id}", tags=["orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = account.read_one(db, item_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.delete(db=db, item_id=menu_item)

#resources
@app.get("/resources/", response_model=list[resources.Resource], tags=["Resource"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resources_id}", response_model=resources.Resource, tags=["Resource"])
def read_one_resource(resources_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, item_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resources_id}", response_model=resources.Resource, tags=["Resource"])
def update_one_resource(resources_id: int, resource: resources.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resource.read_one(db, item_id=resources_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.update(db=db, resource=resource, item_id=resources_id)


@app.delete("/resources/{resources_id}", tags=["Resource"])
def delete_one_resource(resources_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, item_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.delete(db=db, resources_id=resources_id)

#recipes
@app.post("/recipes/", response_model=recipes.Recipe, tags=["Recipe"])
def create_recipe(recipe: recipes.RecipeCreate, db: Session = Depends(get_db)):
    return recipe.create(db=db, recipe=recipe)


@app.get("/recipes/", response_model=list[recipes.Recipe], tags=["Recipe"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipes_id}", response_model=recipes.Recipe, tags=["Recipe"])
def read_one_recipe(recipes_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, item_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipes/{recipes_id}", response_model=recipes.Recipe, tags=["Recipe"])
def update_one_recipe(recipes_id: int, recipe: recipes.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipe.read_one(db, item_id=recipes_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.update(db=db, recipe=recipe, item_id=recipes_id)


@app.delete("/recipes/{recipes_id}", tags=["Recipe"])
def delete_one_recipe(recipes_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, item_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.delete(db=db, item_id=recipes_id)

#order details
@app.post("/order_details/", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def create_order_detail(order_detail: order_details.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_detail.create(db=db, item_id=order_detail)


@app.get("/order_details/", response_model=list[order_details.OrderDetail], tags=["OrderDetail"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get("/order_details/{order_details_id}", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def read_one_order_detail(order_details_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, item_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail


@app.put("/order_details/{order_details_id}", response_model=order_details.OrderDetail, tags=["OrderDetail"])
def update_one_order_detail(order_details_id: int, order_detail: order_details.OrderDetailUpdate,
                            db: Session = Depends(get_db)):
    order_detail_db = order_detail.read_one(db, order_details_id=order_details_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.update(db=db, order_detail=order_detail, order_details_id=order_details_id)


@app.delete("/order_details/{order_details_id}", tags=["OrderDetail"])
def delete_one_order_detail(order_details_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, item_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.delete(db=db, order_details_id=order_details_id)

#accounts
@app.get("/account/", response_model=list[account.Account], tags=["account"])
def read_account(db: Session = Depends(get_db)):
    return account.read_all(db)


@app.get("/account/{account_id}", response_model=account.Account, tags=["account"])
def read_one_account(account_id: int, db: Session = Depends(get_db)):
    accounts = account.read_one(db, item_id=account_id)
    if accounts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return accounts


@app.put("/account/{account_id}", response_model=account.Account, tags=["account"])
def update_one_account(account_id: int, account: account.AccountUpdate, db: Session = Depends(get_db)):
    account_db = account.read_one(db, item_id=account_id)
    if account_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.update(db=db, account=account, item_id=account_id)


@app.delete("/account/{account_id}", tags=["account"])
def delete_one_account(account_id: int, db: Session = Depends(get_db)):
    accounts = account.read_one(db, item_id=account_id)
    if accounts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return account.delete(db=db, item_id=menu_item)

#payment
@app.post("/payment/", response_model=payment.Payment, tags=["payments"])
def create_payments(payment: payment.PaymentCreate, db: Session = Depends(get_db)):
    return payment.create(db=db, payment=payment)


@app.get("/payment/", response_model=list[account.Payment], tags=["payment"])
def read_payment(db: Session = Depends(get_db)):
    return payment.read_all(db)


@app.get("/payment/{payment_id}", response_model=payment.Payment, tags=["payment"])
def read_one_payment(payment_id: int, db: Session = Depends(get_db)):
    payments = payment.read_one(db, item_id=payment_id)
    if payments is None:
        raise HTTPException(status_code=404, detail="User not found")
    return payments


@app.put("/payment/{payment_id}", response_model=payment.Payment, tags=["payment"])
def update_one_payment(payment_id: int, payment: payment.PaymentUpdate, db: Session = Depends(get_db)):
    payment_db = payment.read_one(db, item_id=payment_id)
    if payment_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return payment.update(db=db, payment=payment, item_id=payment_id)


@app.delete("/payment/{payment_id}", tags=["payment"])
def delete_one_payment(payment_id: int, db: Session = Depends(get_db)):
    payments = account.read_one(db, item_id=payment_id)
    if payments is None:
        raise HTTPException(status_code=404, detail="User not found")
    return payment.delete(db=db, item_id=menu_item)

#promotions
@app.post("/promotions/", response_model=promotions.Promotions, tags=["promotions"])
def create_promotions(promotions: promotions.PromotionsCreate, db: Session = Depends(get_db)):
    return promotions.create(db=db, promotions=promotions)


@app.get("/promotions/", response_model=list[promotions.Promotions], tags=["promotions"])
def read_promotions(db: Session = Depends(get_db)):
    return promotions.read_all(db)


@app.get("/promotions/{promotion_id}", response_model=promotions.Promotions, tags=["promotions"])
def read_one_promotions(promotion_id: int, db: Session = Depends(get_db)):
    promotion = promotions.read_one(db, item_id=promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotion


@app.put("/promotions/{promotion_id}", response_model=promotions.Promotions, tags=["promotions"])
def update_one_promotions(promotion_id: int, promotions: promotions.PromotionsUpdate, db: Session = Depends(get_db)):
    promotions_db = promotions.read_one(db, item_id=promotion_id)
    if promotions_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotions.update(db=db, promotions=promotions, item_id=promotion_id)


@app.delete("/promotions/{promotion_id}", tags=["promotions"])
def delete_one_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = promotions.read_one(db, item_id=promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotions.delete(db=db, item_id=promotion_id)

#menu idems
@app.post("/menu_item/", response_model=menu_item.Items, tags=["items"])
def create_item(item: menu_item.ItemsCreate, db: Session = Depends(get_db)):
    return item.create(db=db, item=item)


@app.get("/menu_item/", response_model=list[menu_item.Items], tags=["items"])
def read_items(db: Session = Depends(get_db)):
    return menu_item.read_all(db)


@app.get("/menu_item/{dish_id}", response_model=menu_item.Items, tags=["items"])
def read_one_item(dish_id: int, db: Session = Depends(get_db)):
    item = menu_item.read_one(db, item_id=dish_id)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return item


@app.put("/menu_item/{dish_id}", response_model=menu_item.Items, tags=["items"])
def update_one_item(dish_id: int, item: menu_item.ItemsUpdate, db: Session = Depends(get_db)):
    item_db = item.read_one(db, item_id=dish_id)
    if item_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return item.update(db=db, item=item, item_id=dish_id)


@app.delete("/menu_item/{dish_id}", tags=["items"])
def delete_one_item(dish_id: int, db: Session = Depends(get_db)):
    item = menu_item.read_one(db, item_id=dish_id)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return item.delete(db=db, item_id=dish_id)


model_loader.index()
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
