"""create employee, department, role tables"""
from alembic import op
import sqlalchemy as sa

revision = "0001_create_employee_tables"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("departments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False, unique=True))
    op.create_index("ix_departments_name", "departments", ["name"], unique=False)

    op.create_table("roles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=80), nullable=False, unique=True))
    op.create_index("ix_roles_name", "roles", ["name"], unique=False)

    op.create_table("employees",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("full_name", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("department_id", sa.Integer(), sa.ForeignKey("departments.id", ondelete="SET NULL"), nullable=True),
        sa.Column("manager_id", sa.Integer(), sa.ForeignKey("employees.id", ondelete="SET NULL"), nullable=True))
    op.create_index("ix_employees_full_name", "employees", ["full_name"], unique=False)
    op.create_index("ix_employees_email", "employees", ["email"], unique=False)
    op.create_index("ix_employees_department_id", "employees", ["department_id"], unique=False)
    op.create_index("ix_employees_manager_id", "employees", ["manager_id"], unique=False)

    op.create_table("employee_roles",
        sa.Column("employee_id", sa.Integer(), sa.ForeignKey("employees.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("role_id", sa.Integer(), sa.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True))

def downgrade():
    op.drop_table("employee_roles")
    op.drop_index("ix_employees_manager_id", table_name="employees")
    op.drop_index("ix_employees_department_id", table_name="employees")
    op.drop_index("ix_employees_email", table_name="employees")
    op.drop_index("ix_employees_full_name", table_name="employees")
    op.drop_table("employees")
    op.drop_index("ix_roles_name", table_name="roles")
    op.drop_table("roles")
    op.drop_index("ix_departments_name", table_name="departments")
    op.drop_table("departments")
