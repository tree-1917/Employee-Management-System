from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'company'}
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    age = Column(String(length=100))
    dob = Column(String(length=100))
    email = Column(String(length=100))
    gender = Column(String(length=100))
    contact = Column(String(length=100))
    address = Column(String(length=100))


class Database:
    def __init__(self):
        self.engine = create_engine(
            "mysql+mysqlconnector://root:12345678@localhost:3306/company")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, address):
        new_employee = Employee(
            name=name, age=age, email=email, gender=gender, contact=contact, address=address, dob=dob)
        self.session.add(new_employee)
        self.session.commit()

    def fetch(self):
        results = []
        rows = self.session.query(Employee).all()
        for row in rows:
            results.append((row.id, row.name, row.age, row.dob,
                           row.email, row.gender, row.contact, row.address))
        return results
    # Delete a Record in DB

    def remove(self, id):
        employee_to_delete = self.session.query(
            Employee).filter(Employee.id == id).one()
        self.session.delete(employee_to_delete)
        self.session.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, address):
        employee = self.session.query(Employee).filter(Employee.id == id).one()
        employee.name = name
        employee.age = age
        employee.dob = dob
        employee.email = email
        employee.gender = gender
        employee.contact = contact
        employee.address = address

        self.session.commit()
