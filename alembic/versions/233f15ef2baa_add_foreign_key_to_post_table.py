"""add foreign key to post table

Revision ID: 233f15ef2baa
Revises: 19a6e768d5ad
Create Date: 2023-07-26 08:54:55.408237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '233f15ef2baa'
down_revision = '19a6e768d5ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():  
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')


