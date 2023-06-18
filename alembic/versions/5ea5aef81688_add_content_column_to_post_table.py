"""add content column to post table

Revision ID: 5ea5aef81688
Revises: 08f30e19e072
Create Date: 2023-06-17 17:54:39.111880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea5aef81688'
down_revision = '08f30e19e072'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
