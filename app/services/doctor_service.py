from sqlalchemy.orm import Session
from app.models.doctor import Doctor


def create_doctor(db: Session, doctor_data):
    doctor = Doctor(**doctor_data.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()