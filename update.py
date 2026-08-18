from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Annotated, Literal


class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[
        Optional[Literal["male", "female", "others"]],
        Field(default=None)
    ]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    marriage_status: Annotated[
        Optional[Literal["single", "married"]],
        Field(default=None)
    ]
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact_details: Annotated[Optional[Dict[str, str]], Field(default=None)]