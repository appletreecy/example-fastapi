"""create posts table

Revision ID: 4b941968a00c
Revises: 
Create Date: 2023-06-17 15:56:52.051115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b941968a00c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
