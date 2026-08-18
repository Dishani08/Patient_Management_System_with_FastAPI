# Patient Management System with FastAPI

A simple Patient Management System REST API built using **FastAPI** and **Pydantic**.

The project provides APIs to manage patient information and perform basic patient-related operations.

## Features

- Add and manage patient records
- Get patient details
- Update patient information
- Delete patient records
- Calculate BMI from height and weight
- Sort and filter patient data
- Input validation using Pydantic
- JSON file used as data storage

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON
- Git & GitHub

## Project Structure

```text
Patient_Management_System_with_FastAPI/
│
├── main.py
├── patient_models.py
├── update.py
├── patients.json
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Dishani08/Patient_Management_System_with_FastAPI.git
```

### 2. Navigate to the Project Directory

```bash
cd Patient_Management_System_with_FastAPI
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Data Storage

Patient information is currently stored in:

```text
patients.json
```

This project uses a JSON file instead of a traditional database to keep the project simple and demonstrate REST API development with FastAPI.

## Future Improvements

- Add a database such as MySQL or PostgreSQL
- Add authentication and authorization
- Add a frontend interface
- Dockerize the application
- Deploy the API to a cloud platform

## Author

**Dishani Chauhan**

GitHub: [Dishani08](https://github.com/Dishani08)
