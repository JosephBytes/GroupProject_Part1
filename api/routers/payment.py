from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payment'],
    prefix="/payment"
)


@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{card_number}", response_model=schema.Payment)
def read_one(card_number: int, db: Session = Depends(get_db)):
    return controller.read_one(db, card_number=card_number)


@router.put("/{card_number}", response_model=schema.Payment)
def update(card_number: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, card_number=card_number)


@router.delete("/{card_number}")
def delete(card_number: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, card_number=card_number)
