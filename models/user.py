from sqlalchemy import Column, String, Integer, Numeric, Date, Table, ForeignKey
from datetime import date

# from config.db import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



engine = create_engine("mysql+pymysql://root@localhost:3306/ft")
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

employee_skill_association = Table(
    'employee_skills', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    skills = relationship("Skill", secondary=employee_skill_association, backref="skill")
    salary = Column(Numeric, nullable=False)
    joining_date = Column(Date, nullable=False)


    def __init__(self, name, salary, joining_date):
        self.name = name
        self.salary = salary
        self.joining_date = joining_date

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    employees = relationship("Employee", secondary=employee_skill_association, backref="employee")

    def __init__(self, name):
        self.name = name    

Base.metadata.create_all(engine)

# emp_1 = Employee("Rahul", 10000, date(2018, 10, 11))
# skill_1 = Skill("python")
# skill_2 = Skill("javascript")

# session.add(emp_1)
# session.add(skill_1)
# session.add(skill_2)
# session.commit()
