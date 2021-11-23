"""add user number

Revision ID: 164b165ded3a
Revises: 59b9913e924a
Create Date: 2021-11-23 14:32:41.623156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164b165ded3a'
down_revision = '59b9913e924a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column(
                        'email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
