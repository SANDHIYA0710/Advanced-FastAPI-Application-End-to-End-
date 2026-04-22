from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.doctor import DoctorCreate
from app.services.doctor_service import create_doctor, get_all_doctors
from app.models.doctor import Doctor
from app.utils.auth import verify_token

router = APIRouter(prefix="/doctors", tags=["Doctors"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ CREATE
@router.post("/")
def add_doctor(
    data: DoctorCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return create_doctor(db, data)


# ✅ READ
@router.get("/")
def list_doctors(
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return get_all_doctors(db)


# ✅ UPDATE
@router.put("/{doctor_id}")
def update_doctor(
    doctor_id: int,
    data: DoctorCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.name = data.name
    doctor.specialization = data.specialization
    doctor.email = data.email

    db.commit()
    return doctor


# ✅ DELETE
@router.delete("/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)
    db.commit()

    return {"message": "Doctor deleted"}


# 🔍 FILTER BY SPECIALIZATION (ADD HERE)
@router.get("/filter/")
def filter_doctor(
    specialization: str,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return db.query(Doctor).filter(Doctor.specialization == specialization).all()


# 🔄 ACTIVATE / DEACTIVATE (ADD HERE)
@router.put("/{doctor_id}/toggle")
def toggle_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.is_active = not doctor.is_active
    db.commit()

    return {
        "message": "Doctor status updated",
        "is_active": doctor.is_active
    }