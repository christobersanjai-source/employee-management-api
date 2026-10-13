from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr
    department_id: Optional[int] = None
    manager_id: Optional[int] = None
    role_ids: list[int] = []

class EmployeeRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    department_id: Optional[int] = None
    manager_id: Optional[int] = None
    role_ids: list[int] = []

    model_config = ConfigDict(from_attributes=True)
