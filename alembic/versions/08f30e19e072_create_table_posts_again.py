"""create table posts again

Revision ID: 08f30e19e072
Revises: 4b941968a00c
Create Date: 2023-06-17 17:46:51.161055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08f30e19e072'
down_revision = '4b941968a00c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
