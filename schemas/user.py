from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    id: int
    name: str
    skills: List[str]
    salary: str

    class Config:
        orm_mode = True
