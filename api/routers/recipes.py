from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Recipes'],
    prefix="/recipes"
)

@router.post("/", response_model=schema.Recipes, status_code=status.HTTP_201_CREATED)
def create(request: schema.RecipesCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Recipes])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Recipes)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Recipes)
def update(item_id: int, request: schema.RecipesUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)