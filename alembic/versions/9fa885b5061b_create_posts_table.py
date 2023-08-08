"""create posts table

Revision ID: 9fa885b5061b
Revises: 
Create Date: 2023-07-26 08:02:22.267595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fa885b5061b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    


def downgrade():
    op.drop_table('posts')
    
