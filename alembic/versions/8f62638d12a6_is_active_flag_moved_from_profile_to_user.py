"""is_active flag moved from profile to user

Revision ID: 8f62638d12a6
Revises: f2ff47fff48d
Create Date: 2022-11-05 19:19:40.808665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f62638d12a6'
down_revision = 'f2ff47fff48d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'is_active')
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    op.add_column('profile', sa.Column('is_active', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
