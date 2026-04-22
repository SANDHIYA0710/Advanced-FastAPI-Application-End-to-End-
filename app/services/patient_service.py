from app.models.patient import Patient

def create_patient(db, data):
    try:
        new_patient = Patient(
            name=data.name,
            phone=data.phone
        )

        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)

        return new_patient

    except Exception as e:
        db.rollback()
        return {"error": str(e)}