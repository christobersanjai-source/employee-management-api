# Employee Management API — Task 2

A layered FastAPI project demonstrating SQLAlchemy models and relationships for employees, departments, and roles.

## Technology

- Python + FastAPI: HTTP API
- SQLAlchemy 2: ORM models and relationships
- PostgreSQL: relational database
- Alembic: versioned schema migrations
- Docker Compose: runs API and database
- pytest: automated tests

## Features

- Create and retrieve employees.
- Update and delete employee records.
- Create and retrieve departments.
- Create and retrieve roles.
- Support employee-manager relationships.
- Support many-to-many employee-role relationships.
- Validate request data using Pydantic schemas.
- Manage database schema using Alembic migrations.
- Run the API and database using Docker Compose.

## Data Design

- One department can have many employees.
- An employee can optionally report to another employee using `manager_id`.
- Employees and roles have a many-to-many relationship through `employee_roles`.
- Employee email is unique and indexed.
- Department and manager IDs are indexed for lookup.
- Role and department names are unique.

## Prerequisites

- Python
- Docker Desktop
- Git (optional)

## Setup and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/christobersanjai-source/employee-management-api.git
   cd employee-management-api
   ```

2. Copy `.env.example` to `.env` and configure the required environment variables.

3. Start Docker Desktop.

4. Start the application:

   ```bash
   docker compose up --build
   ```

5. Open the API:

   - Health check: `http://localhost:8001/health`
   - Interactive API documentation: `http://localhost:8001/docs`

**Note:** The API uses local port `8001` in the current Docker Compose configuration. Update these URLs if you change the port mapping.

The API container runs `alembic upgrade head` before starting FastAPI.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/departments` | Retrieve departments |
| POST | `/departments` | Create a department |
| GET | `/roles` | Retrieve roles |
| POST | `/roles` | Create a role |
| GET | `/employees` | Retrieve employees |
| POST | `/employees` | Create an employee |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |

## Example Employee Request

**POST** `/employees`

```json
{
  "full_name": "Kumar",
  "email": "kumar@example.com",
  "department_id": 1,
  "manager_id": null,
  "role_ids": [1]
}
```

Use the interactive API documentation to test the endpoints and view the required fields.

## Tests

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -q
```

The model tests use an in-memory SQLite database. The test command may depend on your environment configuration.

## Database Migrations

Alembic is used to manage database schema changes. The Docker startup process runs migrations before starting the API.

## Project Documentation

- Sample data: `sample_data/employees.json`
- API contract: `docs/api_contract.md`
- Entity relationship diagram: `docs/er_diagram.md`

## Security

- Keep `.env` private.
- Never commit passwords or secret keys.
- Use `.env.example` to document required environment variables without exposing real credentials.

## Author

Christober Sanjai S.