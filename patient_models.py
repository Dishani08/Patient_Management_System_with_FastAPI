from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    computed_field,
    field_validator,
    model_validator,
)
from typing import List, Optional, Annotated, Literal


class ContactDetails(BaseModel):
    email: EmailStr
    ph_no: str
    emergency: Optional[str] = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError(
                "Email domain must be either hdfc.com or icici.com"
            )

        return value


class Patient(BaseModel):
    id: str
    name: str = Field(max_length=50)
    city: str
    age: int = Field(gt=0)
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(description="Gender of the patient"),
    ]
    height: float = Field(gt=0)
    weight: float = Field(gt=0)
    marriage_status: bool = False
    allergies: Optional[List[str]] = None
    contact_details: ContactDetails

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    @model_validator(mode="after")
    def validate_emergency_contact(self):

        if self.age > 60 and self.contact_details.emergency is None:
            raise ValueError(
                "Patients older than 60 must have an emergency contact."
            )

        return self

    def insert_patient_data(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("City:", self.city)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Marriage Status:", self.marriage_status)
        print("Allergies:", self.allergies)
        print("Contact Details:", self.contact_details.model_dump())
        print("BMI:", self.bmi)
        print("Verdict:", self.verdict)