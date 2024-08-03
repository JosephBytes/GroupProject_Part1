from fastapi import FastAPI, HTTPException, APIRouter, Depends, status
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
    try:
        new_account = controller.create(db=db, request=request)
        if new_account is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return new_account
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/", response_model=list[Account])
def read_all(db: Session = Depends(get_db)):
    try:
        all_accounts = controller.read_all(db)
        if all_accounts is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return all_accounts
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/{account_id}", response_model=Account)
def read_one(account_id: int, db: Session = Depends(get_db)):
    try:
        acct = controller.read_one(db, account_id=account_id)
        if acct is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return acct
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.put("/{account_id}", response_model=Account)
def update(account_id: int, request: AccountUpdate, db: Session = Depends(get_db)):
    try:
        updated = controller.update(db=db, request=request, account_id=account_id)
        if updated is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return updated
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(account_id: int, db: Session = Depends(get_db)):
    try:
        deleted = controller.delete(db=db, account_id=account_id)
        if deleted is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return deleted
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

