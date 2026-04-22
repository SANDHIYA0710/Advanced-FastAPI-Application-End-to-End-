from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.database import SessionLocal
from app.schemas.appointment import AppointmentCreate
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.utils.auth import verify_token

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ CREATE APPOINTMENT
@router.post("/")
def add_appointment(
    data: AppointmentCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    patient = db.query(Patient).filter(Patient.id == data.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_appointment = Appointment(
        doctor_id=data.doctor_id,
        patient_id=data.patient_id,
        appointment_time=data.appointment_time
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    # ✅ LOGGING ADDED HERE
    logging.info(f"Appointment created: ID={new_appointment.id}, Doctor={doctor.name}, Patient={patient.name}")

    return {
        "message": "Appointment created successfully",
        "data": {
            "id": new_appointment.id,
            "doctor_name": doctor.name,
            "patient_name": patient.name,
            "appointment_time": new_appointment.appointment_time,
            "status": new_appointment.status
        }
    }


# ✅ GET ALL APPOINTMENTS
@router.get("/")
def list_appointments(
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    appointments = db.query(Appointment).all()

    result = []
    for a in appointments:
        doctor = db.query(Doctor).filter(Doctor.id == a.doctor_id).first()
        patient = db.query(Patient).filter(Patient.id == a.patient_id).first()

        result.append({
            "id": a.id,
            "doctor_name": doctor.name,
            "patient_name": patient.name,
            "appointment_time": a.appointment_time,
            "status": a.status
        })

    return result


# ✅ GET BY DOCTOR
@router.get("/doctor/{doctor_id}")
def get_by_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    appointments = db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found")

    result = []

    for a in appointments:
        doctor = db.query(Doctor).filter(Doctor.id == a.doctor_id).first()
        patient = db.query(Patient).filter(Patient.id == a.patient_id).first()

        result.append({
            "id": a.id,
            "doctor_name": doctor.name,
            "patient_name": patient.name,
            "appointment_time": a.appointment_time,
            "status": a.status
        })

    return result


# ✅ GET BY PATIENT
@router.get("/patient/{patient_id}")
def get_by_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    appointments = db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found")

    result = []

    for a in appointments:
        doctor = db.query(Doctor).filter(Doctor.id == a.doctor_id).first()
        patient = db.query(Patient).filter(Patient.id == a.patient_id).first()

        result.append({
            "id": a.id,
            "doctor_name": doctor.name,
            "patient_name": patient.name,
            "appointment_time": a.appointment_time,
            "status": a.status
        })

    return result


# ❌ CANCEL APPOINTMENT
@router.put("/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = "Cancelled"
    db.commit()

    # ✅ LOGGING ADDED HERE
    logging.info(f"Appointment cancelled: ID={appointment_id}")

    return {"message": "Appointment cancelled successfully"}