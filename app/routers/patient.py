from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.patient import PatientCreate
from app.services.patient_service import create_patient
from app.models.patient import Patient
from app.utils.auth import verify_token

router = APIRouter(prefix="/patients", tags=["Patients"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ CREATE
@router.post("/")
def add_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return create_patient(db, data)


# 🔍 SEARCH
@router.get("/search/")
def search_patient(
    name: str,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return db.query(Patient).filter(Patient.name.contains(name)).all()


# 📄 LIST (Pagination)
@router.get("/")
def list_patients(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return db.query(Patient).offset(skip).limit(limit).all()


# ✏️ UPDATE (ADD THIS)
@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    data: PatientCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient.name = data.name
    patient.phone = data.phone

    db.commit()

    return {
        "message": "Patient updated successfully",
        "data": patient
    }


# ❌ DELETE (ADD THIS)
@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()

    return {"message": "Patient deleted successfully"}