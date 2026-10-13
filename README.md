# Employee Management API — Task 2

A RESTful API built using FastAPI, SQLAlchemy, and PostgreSQL to manage employees, departments, and roles. This project demonstrates layered application structure, database relationships, migrations, and automated testing.

## Features

- Create and retrieve employees.
- Update and delete employee records.
- Create and retrieve departments.
- Create and retrieve roles.
- Support employee-manager relationships.
- Support many-to-many relationships between employees and roles.
- Validate API requests using Pydantic schemas.
- Manage database schema using Alembic migrations.
- Run the application and database using Docker Compose.
- Include automated tests using pytest.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- Alembic
- Docker and Docker Compose
- pytest

## Project Structure

```text
employee_management_task2/
├── app/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── main.py
│   └── schemas.py
├── alembic/
│   └── versions/
├── docs/
│   ├── api_contract.md
│   └── er_diagram.md
├── sample_data/
│   └── employees.json
├── tests/
├── .env.example
├── .gitignore
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Database Relationships

- One department can have multiple employees.
- An employee can optionally report to another employee through `manager_id`.
- Employees and roles have a many-to-many relationship through `employee_roles`.
- Employee email addresses are unique and indexed.
- Department and role names are unique.

## Prerequisites

- Python installed
- Docker Desktop installed and running
- Git (optional, for version control)

## Setup and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/christobersanjai-source/employee-management-api.git
   cd employee-management-api
   ```

2. Copy `.env.example` to `.env` and configure the required environment variables.

3. Start the application:

   ```bash
   docker compose up --build
   ```

4. Open the API endpoints:

   - Health check: `http://localhost:8001/health`
   - Interactive API documentation: `http://localhost:8001/docs`

**Note:** The local API port is configured as `8001` in this project. If you change the port mapping in `docker-compose.yml`, update these URLs accordingly.

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

Use the interactive documentation at `/docs` to test requests and view the required fields.

## Running Tests

Activate your Python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -q
```

The model tests use an in-memory SQLite database. Run the tests in your configured environment to verify the complete test setup.

## Database Migrations

The application uses Alembic to manage database schema changes. The Docker startup command runs migrations before starting the API.

## Sample Data and Documentation

- Sample employee data: `sample_data/employees.json`
- API contract: `docs/api_contract.md`
- Entity relationship diagram: `docs/er_diagram.md`

## Security

- Keep `.env` private.
- Do not commit passwords, secret keys, or other credentials.
- Use `.env.example` to document the required environment variables without exposing real secrets.

## Author

Christober Sanjai S.