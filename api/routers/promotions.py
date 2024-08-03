from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)


@router.post("/", response_model=schema.Promotions)
def create(request: schema.PromotionsCreate, db: Session = Depends(get_db)):
    try:
        new_promo = controller.create(db=db, request=request)
        if new_promo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return new_promo
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/", response_model=list[schema.Promotions])
def read_all(db: Session = Depends(get_db)):
    try:
        all_promos = controller.read_all(db)
        if all_promos is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return all_promos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/{promotion_id}", response_model=schema.Promotions)
def read_one(promotion_id: int, db: Session = Depends(get_db)):
    try:
        promo = controller.read_one(db, promotion_id=promotion_id)
        if promo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )
        return promo
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.put("/{promotion_id}", response_model=schema.Promotions)
def update(promotion_id: int, request: schema.PromotionsUpdate, db: Session = Depends(get_db)):
    try:
        updated = controller.update(db=db, request=request, promotion_id=promotion_id)
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


@router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(promotion_id: int, db: Session = Depends(get_db)):
    try:
        deleted = controller.delete(db=db, promotion_id=promotion_id)
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

