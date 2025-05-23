"""Renaming students to scholars

Revision ID: 67ce9d903e59
Revises: 45ce06ad8f25
Create Date: 2025-05-23 16:45:07.845985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67ce9d903e59'
down_revision = '45ce06ad8f25'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
