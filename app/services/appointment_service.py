from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient

def create_appointment(db, data):
    # check doctor
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        return {"error": "Doctor not found"}

    # check patient
    patient = db.query(Patient).filter(Patient.id == data.patient_id).first()
    if not patient:
        return {"error": "Patient not found"}

    new_appointment = Appointment(
        doctor_id=data.doctor_id,
        patient_id=data.patient_id,
        appointment_date=data.appointment_date
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment