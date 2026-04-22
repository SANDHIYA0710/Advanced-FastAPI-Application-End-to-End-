from pydantic import BaseModel, EmailStr

# used when creating doctor
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr

# used when returning doctor response
class DoctorResponse(DoctorCreate):
    id: int

    class Config:
        from_attributes = True