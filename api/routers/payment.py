from fastapi import APIRouter, Depends, HTTPException, status, Response
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
    try:
        new_payment = controller.create(db=db, request=request)
        if new_payment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return new_payment
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    try:
        all_payments = controller.read_all(db)
        if all_payments is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return all_payments
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/payment/{card_number}", response_model=schema.Payment)
def read_one(card_number: int, db: Session = Depends(get_db)):
    try:
        pmt = controller.read_one(db, card_number=card_number)
        if pmt is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return pmt
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.put("/payment/{card_number}", response_model=schema.Payment)
def update(card_number: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    try:
        updated = controller.update(db=db, request=request, card_number=card_number)
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


@router.delete("/payment/{card_number}")
def delete(card_number: int, db: Session = Depends(get_db)):
    try:
        deleted = controller.delete(db=db, card_number=card_number)
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
