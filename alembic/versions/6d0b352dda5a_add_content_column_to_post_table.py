"""add content column to post table

Revision ID: 6d0b352dda5a
Revises: 9fa885b5061b
Create Date: 2023-07-26 08:11:54.646216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d0b352dda5a'
down_revision = '9fa885b5061b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    

def downgrade() -> None:
    op.drop_column('posts', 'content')
