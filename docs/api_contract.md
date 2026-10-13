# Employee Management API Contract

Base URL: http://localhost:8001

## Health Check
GET /health
Returns API status.

## Departments
GET /departments
Returns all departments.

POST /departments
Request:
{
  "name": "IT"
}

## Roles
GET /roles
Returns all roles.

POST /roles
Request:
{
  "name": "Python Developer"
}

## Employees
GET /employees
Returns all employees.

POST /employees
Request:
{
  "full_name": "Arun Kumar",
  "email": "arun.kumar@example.com",
  "department_id": 1,
  "manager_id": null,
  "role_ids": [1]
}

Successful creation returns HTTP 201.
