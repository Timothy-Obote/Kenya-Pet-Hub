# app/routers/pets.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from .auth import get_current_user

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/", response_model=list[schemas.PetOut])
def list_pets(db: Session = Depends(get_db)):
    return db.execute(select(models.Pet)).scalars().all()

@router.get("/{pet_id}", response_model=schemas.PetOut)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.execute(select(models.Pet).filter_by(id=pet_id)).scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.post("/", response_model=schemas.PetOut, status_code=status.HTTP_201_CREATED)
def create_pet(pet_in: schemas.PetCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    pet = models.Pet(**pet_in.model_dump(), owner_id=current_user.id)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

@router.put("/{pet_id}", response_model=schemas.PetOut)
def update_pet(pet_id: int, pet_in: schemas.PetCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    pet = db.execute(select(models.Pet).filter_by(id=pet_id)).scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if pet.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    for k, v in pet_in.model_dump().items():
        setattr(pet, k, v)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet(pet_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    pet = db.execute(select(models.Pet).filter_by(id=pet_id)).scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if pet.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    db.delete(pet)
    db.commit()
    return {}
