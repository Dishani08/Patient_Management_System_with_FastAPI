# FastAPI heavily depends on Starlette and Pydantic

from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from patient_models import Patient
from update import PatientUpdate
import json

app = FastAPI()


#  Utility Functions 

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


#  Basic Routes 

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {
        "comment": "A fully functional API to manage your patient records"
    }


@app.get("/view")
def view():
    return load_data()


#  View One Patient 

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(...,description="ID of the patient in the database",example="P001",)):

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


#  Sort Patients 

@app.get("/sort")
def sort_patients(sort_by: str = Query(...,description="Sort on the basis of height, weight or bmi"),order: str = Query("asc",description="Sort in asc or desc order")):

    if sort_by not in ["height", "weight", "bmi"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid field. Choose height, weight or bmi."
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc."
        )

    data = load_data()

    reverse_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )

    return sorted_data


#  Create Patient 

@app.post("/create")
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    data[patient.id] = patient.model_dump(exclude={"id"})

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient created successfully" }
    )


# Update Patient 

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Add id temporarily
    existing_patient_info["id"] = patient_id

    # Recalculate BMI & Verdict automatically
    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(
        exclude={"id"}
    )

    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient details updated successfully"
        }
    )


#  Delete Patient 

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    del data[patient_id]

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient deleted successfully"
        }
    )