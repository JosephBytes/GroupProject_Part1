from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import account as controller
from ..schemas.account import Account, AccountCreate, AccountUpdate
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Account'],
    prefix="/account"
)


@router.post("/", response_model=Account, status_code=status.HTTP_201_CREATED)
def create(request: AccountCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[Account])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{account_id}", response_model=Account)
def read_one(account_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, account_id=account_id)


@router.put("/{account_id}", response_model=Account)
def update(account_id: int, request: AccountUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, account_id=account_id)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(account_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, account_id=account_id)

