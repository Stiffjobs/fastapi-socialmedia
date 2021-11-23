"""add content column to posts table

Revision ID: 59b9913e924a
Revises: cbd0dd2a388f
Create Date: 2021-11-23 13:23:54.612137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59b9913e924a'
down_revision = 'cbd0dd2a388f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
