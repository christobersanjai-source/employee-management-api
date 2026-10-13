# Employee Management API — Task 2

A layered FastAPI project demonstrating SQLAlchemy models and relationships for employees, departments, and roles.

## Technology
- Python + FastAPI: HTTP API
- SQLAlchemy 2: ORM models and relationships
- PostgreSQL: relational database
- Alembic: versioned schema migrations
- Docker Compose: runs API and database
- pytest: automated tests

## Data design
- One department can have many employees.
- An employee can optionally report to another employee (`manager_id` self-reference).
- Employees can have multiple roles; roles can be assigned to multiple employees through `employee_roles`.
- Employee email is unique and indexed.
- Department/manager IDs are indexed for lookup.
- Role and department names are unique.

## Start
1. Copy `.env.example` to `.env`.
2. Start Docker Desktop.
3. Run `docker compose up --build`.
4. API health: `http://localhost:8000/health`
5. Interactive docs: `http://localhost:8000/docs`

The API container runs `alembic upgrade head` before starting FastAPI.

## Tests
Create a virtual environment and install dependencies:
`pip install -r requirements.txt`
Then run:
`pytest -q`

The model tests use an in-memory SQLite database so they can run without PostgreSQL.

## Example employee request
POST `/employees`
```json
{
  "full_name": "Kumar",
  "email": "kumar@example.com",
  "department_id": 1,
  "manager_id": 1,
  "role_ids": [1]
}
```

## Important
This is a starter implementation for the internship task. Verify it in your environment, update any existing Task 1 files carefully, and do not submit until Docker startup, migrations, and tests have been run successfully.
