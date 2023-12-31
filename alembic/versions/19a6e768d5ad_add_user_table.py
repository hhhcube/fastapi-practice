"""add user table

Revision ID: 19a6e768d5ad
Revises: 6d0b352dda5a
Create Date: 2023-07-26 08:35:21.568613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19a6e768d5ad'
down_revision = '6d0b352dda5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')          
                    )


def downgrade() -> None:
    op.drop_table('users')
    pass
