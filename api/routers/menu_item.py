from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu_item'],
    prefix="/menu_item"
)


@router.post("/", response_model=schema.Items)
def create(request: schema.ItemsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Items])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{dish_id}", response_model=schema.Items)
def read_one(dish_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, dish_id=dish_id)


@router.put("/{dish_id}", response_model=schema.Items)
def update(dish_id: int, request: schema.ItemsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, dish_id=dish_id)


@router.delete("/{dish_id}")
def delete(dish_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, dish_id=dish_id)
