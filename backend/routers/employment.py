from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import get_db
from models import Employment

router = APIRouter()

class EmploymentCreate(BaseModel):
    agent_id: int
    position: str
    start_date: str
    end_date: str

class EmploymentResponse(BaseModel):
    id: int
    agent_id: int
    position: str
    start_date: str
    end_date: str

@router.post("/", response_model=EmploymentResponse)
def create_employment(employment: EmploymentCreate, db: Session = Depends(get_db)):
    db_employment = Employment(**employment.dict())
    db.add(db_employment)
    db.commit()
    db.refresh(db_employment)
    return db_employment

@router.get("/", response_model=List[EmploymentResponse])
def read_employment(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employment_records = db.query(Employment).offset(skip).limit(limit).all()
    return employment_records

@router.get("/{employment_id}", response_model=EmploymentResponse)
def read_employment_by_id(employment_id: int, db: Session = Depends(get_db)):
    employment_record = db.query(Employment).filter(Employment.id == employment_id).first()
    if employment_record is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    return employment_record

@router.put("/{employment_id}", response_model=EmploymentResponse)
def update_employment(employment_id: int, employment: EmploymentCreate, db: Session = Depends(get_db)):
    db_employment = db.query(Employment).filter(Employment.id == employment_id).first()
    if db_employment is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    for key, value in employment.dict().items():
        setattr(db_employment, key, value)
    db.commit()
    db.refresh(db_employment)
    return db_employment

@router.delete("/{employment_id}", response_model=EmploymentResponse)
def delete_employment(employment_id: int, db: Session = Depends(get_db)):
    db_employment = db.query(Employment).filter(Employment.id == employment_id).first()
    if db_employment is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    db.delete(db_employment)
    db.commit()
    return db_employment
