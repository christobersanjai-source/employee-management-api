
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.models import Employee, Department, Role
from app.schemas import EmployeeCreate

app = FastAPI(title="Employee Management API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/departments")
def list_departments(db: Session = Depends(get_db)):
    return db.query(Department).order_by(Department.id).all()


@app.post("/departments", status_code=201)
def create_department(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("name")
    if not name or not name.strip():
        raise HTTPException(status_code=400, detail="Department name is required")

    department = Department(name=name.strip())
    db.add(department)

    try:
        db.commit()
        db.refresh(department)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Department could not be created")

    return {"id": department.id, "name": department.name}


@app.get("/roles")
def list_roles(db: Session = Depends(get_db)):
    return db.query(Role).order_by(Role.id).all()


@app.post("/roles", status_code=201)
def create_role(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("name")
    if not name or not name.strip():
        raise HTTPException(status_code=400, detail="Role name is required")

    role = Role(name=name.strip())
    db.add(role)

    try:
        db.commit()
        db.refresh(role)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Role could not be created")

    return {"id": role.id, "name": role.name}


@app.get("/employees")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).order_by(Employee.id).all()


@app.post("/employees", status_code=201)
def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    if payload.department_id is not None and not db.get(
        Department, payload.department_id
    ):
        raise HTTPException(status_code=404, detail="Department not found")

    if payload.manager_id is not None and not db.get(
        Employee, payload.manager_id
    ):
        raise HTTPException(status_code=404, detail="Manager not found")

    roles = []
    for role_id in payload.role_ids:
        role = db.get(Role, role_id)
        if not role:
            raise HTTPException(
                status_code=404,
                detail=f"Role {role_id} not found",
            )
        roles.append(role)

    employee = Employee(
        full_name=payload.full_name,
        email=str(payload.email).lower(),
        department_id=payload.department_id,
        manager_id=payload.manager_id,
        roles=roles,
    )
    db.add(employee)

    try:
        db.commit()
        db.refresh(employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists or data constraint failed",
        )

    return {
        "id": employee.id,
        "full_name": employee.full_name,
        "email": employee.email,
        "department_id": employee.department_id,
        "manager_id": employee.manager_id,
        "role_ids": [role.id for role in employee.roles],
    }

@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    payload: EmployeeCreate,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if payload.department_id is not None and not db.get(
        Department, payload.department_id
    ):
        raise HTTPException(status_code=404, detail="Department not found")

    if payload.manager_id is not None:
        if payload.manager_id == employee_id:
            raise HTTPException(
                status_code=400, detail="Employee cannot be their own manager"
            )
        if not db.get(Employee, payload.manager_id):
            raise HTTPException(status_code=404, detail="Manager not found")

    roles = []
    for role_id in payload.role_ids:
        role = db.get(Role, role_id)
        if not role:
            raise HTTPException(
                status_code=404, detail=f"Role {role_id} not found"
            )
        roles.append(role)

    employee.full_name = payload.full_name
    employee.email = str(payload.email).lower()
    employee.department_id = payload.department_id
    employee.manager_id = payload.manager_id
    employee.roles = roles

    try:
        db.commit()
        db.refresh(employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists or data constraint failed",
        )

    return {
        "id": employee.id,
        "full_name": employee.full_name,
        "email": employee.email,
        "department_id": employee.department_id,
        "manager_id": employee.manager_id,
        "role_ids": [role.id for role in employee.roles],
    }


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Employee cannot be deleted because it is referenced by another record",
        )

    return None

