from fastapi import FastAPI
from app.database import Base, engine
import logging

logging.basicConfig(level=logging.INFO)

from app.routers import doctor as doctor_router
from app.routers import patient as patient_router
from app.routers import appointment as appointment_router
from app.routers import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(doctor_router.router)
app.include_router(patient_router.router)
app.include_router(appointment_router.router)
app.include_router(auth.router)