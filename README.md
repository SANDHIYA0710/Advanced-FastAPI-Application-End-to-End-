
# Advanced-FastAPI-Application-(End-to-End)

## Project Overview

This project is a Hospital Management Backend System built using FastAPI.
It extends basic CRUD APIs into a fully functional real-world backend application with authentication, modular architecture, and multiple features.

The system manages:

* Doctors
* Patients
* Appointments

---

## Objective

To design and implement a scalable, modular, and secure backend system using FastAPI, SQLAlchemy, and JWT authentication.

---

## Tech Stack

* Backend Framework: FastAPI
* Database: SQLite
* ORM: SQLAlchemy
* Authentication: JWT (JSON Web Token)
* Validation: Pydantic
* Server: Uvicorn
* Language: Python

---

## Project Structure

```id="qjb9bo"
app/
│
├── models/          # Database models (SQLAlchemy)
├── schemas/         # Pydantic schemas (validation)
├── routers/         # API routes
├── services/        # Business logic
├── utils/           # Auth, hashing, helpers
├── core/            # Config / env (if used)
│
├── database.py      # DB connection
├── main.py          # Entry point
│
├── .env.example     # Environment variables template
├── requirements.txt # Dependencies
├── README.md        # Project documentation
```

---

## Authentication Module

* JWT-based authentication
* Login API to generate token
* All APIs are protected except login

### Login Endpoint

```id="ypy4ud"
POST /login
```

---

## Doctor Module

### Features:

* Create Doctor
* Update Doctor
* Delete Doctor
* Get All Doctors
* Filter by Specialization
* Activate / Deactivate Doctor

### Endpoints:

```id="qudk5b"
POST    /doctors/
GET     /doctors/
PUT     /doctors/{doctor_id}
DELETE  /doctors/{doctor_id}
GET     /doctors/filter/?specialization=
PUT     /doctors/{doctor_id}/toggle
```

---

## Patient Module

### Features:

* Create Patient
* Update Patient
* Delete Patient
* Search by Name / Phone
* Pagination support

### Endpoints:

```id="4jvc9k"
POST    /patients/
GET     /patients/
PUT     /patients/{patient_id}
DELETE  /patients/{patient_id}
GET     /patients/search/?name=
```

---

## Appointment Module

### Features:

* Create Appointment (Doctor ↔ Patient)
* Get All Appointments
* Get by Doctor
* Get by Patient
* Cancel Appointment

### Appointment Fields:

* doctor_id
* patient_id
* appointment_time
* status (Scheduled / Completed / Cancelled)

### Endpoints:

```id="cl1ln4"
POST    /appointments/
GET     /appointments/
GET     /appointments/doctor/{doctor_id}
GET     /appointments/patient/{patient_id}
PUT     /appointments/{appointment_id}/cancel
```

---

## Additional Features

* Pagination (Patients list)
* Logging implemented
* Environment variables using `.env`
* Clean modular architecture
* Structured folder design

---

## Error Handling

* Proper HTTP status codes
* Uses HTTPException for errors
* Validations handled using Pydantic

Example:

```id="lu3e12"
404 → Doctor not found
401 → Unauthorized
422 → Validation error
```

---

## Setup Instructions

### 1. Clone Repository

```id="x5pg3d"
git clone https://github.com/SANDHIYA0710/Advanced-FastAPI-Application-End-to-End-.git
cd Advanced-FastAPI-Application-End-to-End-
```

---

### 2. Create Virtual Environment

```id="5fj3o4"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```id="ogc7l9"
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env` file:

```id="uxnvbn"
DATABASE_URL=sqlite:///./hospital.db
SECRET_KEY=your_secret_key
```

---

### 5. Run Server

```id="5zlhcx"
uvicorn app.main:app --reload
```

---

### 6. Open API Documentation

```id="pew0ur"
http://127.0.0.1:8000/docs
```

---

## API Testing

* Swagger UI available at `/docs`
* Postman can be used for testing

---

## Bonus Features

* Role-based access (if implemented)
* Improved API response formatting
* Logging support

---

## Submission Includes

* GitHub Repository
* README Documentation
* Working APIs
* Clean Code Structure

---

## Future Improvements

* Docker support
* MySQL/PostgreSQL integration
* Frontend integration
* Role-based dashboards

---

## Final Note

This project demonstrates:

* Backend architecture design
* API development using FastAPI
* Authentication and security
* Real-world application structure

---

