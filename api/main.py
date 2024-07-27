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
from .controllers import orders
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
@app.post("/orders/", response_model=orders.Order, tags=["Orders"])
def create_order(order: orders.OrdersCreate, db: Session):
    return order.create(db=db, orders=orders)


@app.get("/orders/", response_model=list[orders.Order], tags=["Orders"])
def read_orders(db: Session):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=orders.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=orders.Order, tags=["Orders"])
def update_one_order(order_id: int, order: orders.OrderUpdate, db: Session):
    order_db = orders.read_one(db, item_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, item_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session):
    order = orders.read_one(db, item_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, item_id=menu_item)


model_loader.index()
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
