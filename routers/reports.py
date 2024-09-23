from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import get_db
from models import Report

router = APIRouter()

class ReportCreate(BaseModel):
    agent_id: int
    report_data: str

class ReportResponse(BaseModel):
    id: int
    agent_id: int
    report_data: str

@router.post("/", response_model=ReportResponse)
def create_report(report: ReportCreate, db: Session = Depends(get_db)):
    db_report = Report(
        agent_id=report.agent_id,
        report_data=report.report_data
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@router.get("/", response_model=List[ReportResponse])
def read_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = db.query(Report).offset(skip).limit(limit).all()
    return reports

@router.get("/{report_id}", response_model=ReportResponse)
def read_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.put("/{report_id}", response_model=ReportResponse)
def update_report(report_id: int, report: ReportCreate, db: Session = Depends(get_db)):
    db_report = db.query(Report).filter(Report.id == report_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    db_report.agent_id = report.agent_id
    db_report.report_data = report.report_data
    db.commit()
    db.refresh(db_report)
    return db_report

@router.delete("/{report_id}", response_model=ReportResponse)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    db_report = db.query(Report).filter(Report.id == report_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    db.delete(db_report)
    db.commit()
    return db_report
