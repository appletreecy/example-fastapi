"""add last few columns to posts table

Revision ID: 19d261a7a556
Revises: e4cb9c7d1bcb
Create Date: 2023-06-17 18:35:10.008901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19d261a7a556'
down_revision = 'e4cb9c7d1bcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('post', 'published')
    op.drop_column('post', 'created_at')
    pass
