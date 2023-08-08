"""add last few columns to posts table

Revision ID: e6d9aeb818ce
Revises: 233f15ef2baa
Create Date: 2023-07-26 09:11:41.159666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6d9aeb818ce'
down_revision = '233f15ef2baa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))

def downgrade() -> None:
    op.drop_column('posts', "published")
    op.drop_column('posts', 'created_at')
