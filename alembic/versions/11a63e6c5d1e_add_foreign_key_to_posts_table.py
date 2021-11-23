"""add foreign-key to posts table

Revision ID: 11a63e6c5d1e
Revises: 164b165ded3a
Create Date: 2021-11-23 15:19:40.413673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11a63e6c5d1e'
down_revision = '164b165ded3a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
