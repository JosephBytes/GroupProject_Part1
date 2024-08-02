from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas.orders import Order, OrderCreate, OrderUpdate
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=Order)
def create(request: OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{order_id}", response_model=Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)


@router.put("/{order_id}", response_model=Order)
def update(order_id: int, request: OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)


@router.delete("/{order_id}", response_model=None)
def delete(order_id: int,  db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)
