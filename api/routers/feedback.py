from fastapi import FastAPI, HTTPException, APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import account as controller
from ..schemas.feedback import Feedback, FeedbackCreate, FeedbackUpdate
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Feedback'],
    prefix="/feedback"
)


@router.post("/", response_model=Feedback, status_code=status.HTTP_201_CREATED)
def create(request: FeedbackCreate, db: Session = Depends(get_db)):
    try:
        new_review = controller.create(db=db, request=request)
        if new_review is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )
        return new_review
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/", response_model=list[Feedback])
def read_all(db: Session = Depends(get_db)):
    try:
        all_reviews = controller.read_all(db)
        if all_reviews is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )
        return all_reviews
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/{review_id}", response_model=Feedback)
def read_one(review_id: int, db: Session = Depends(get_db)):
    try:
        fb = controller.read_one(db, account_id=review_id)
        if fb is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )
        return fb
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.put("/{review_id}", response_model=Feedback)
def update(review_id: int, request: FeedbackUpdate, db: Session = Depends(get_db)):
    try:
        updated = controller.update(db=db, request=request, account_id=review_id)
        if updated is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )
        return updated
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(review_id: int, db: Session = Depends(get_db)):
    try:
        deleted = controller.delete(db=db, account_id=review_id)
        if deleted is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )
        return deleted
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

