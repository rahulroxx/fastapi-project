from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

from models.user import Session
import models.user as models

app = FastAPI()
session = Session()


class Employee(BaseModel):
    id: int
    name: str
    skills: List[str]
    salary: int
    joining_date: date

    class Config:
        orm_mode = True


@app.get('/employees', response_model=List[Employee], status_code=200)
async def get_all_employees():
    employees = session.query(models.Employee).all()
    return employees

@app.get('/employees/{employee_id}')
async def get_employee(employee_id: int):
    pass

@app.post('/employees')
async def create_an_employee(emp: Employee):

    old_skills = []
    new_skills = lambda x: x if not (session.query(models.Skill).filter_by(name=x).all()) else old_skills.append(x)

    new_emp = models.Employee(
        name=emp.name,
        salary=emp.salary,
        joining_date=emp.joining_date
    )

    new_skill_instances = [models.Skill(name=x) for x in filter(new_skills, emp.skills)]
    session.add_all(new_skill_instances)

    #Associate with each employee
    old_skill_instances = [session.query(models.Skill).filter_by(name=x).one() for x in old_skills]
    total_skill_instances = new_skill_instances + old_skill_instances

    new_emp.skills = total_skill_instances
    print(total_skill_instances)

    session.add(new_emp)
    session.commit()

    return