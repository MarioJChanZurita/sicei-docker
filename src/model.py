from pydantic import Field, BaseModel
from typing import Optional

class Student(BaseModel):
    id: int = Field(...)
    nombre: str = Field(...)
    matricula: str = Field(...)

class StudentUpdate(BaseModel):
    nombre: Optional[str]
    matricula: Optional[str]