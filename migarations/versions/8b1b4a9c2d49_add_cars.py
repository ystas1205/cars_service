"""Add cars

Revision ID: 8b1b4a9c2d49
Revises: 
Create Date: 2024-09-25 19:41:11.338291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b1b4a9c2d49'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('year_of_issue', sa.Integer(), nullable=False),
    sa.Column('fuel_type', sa.String(length=50), nullable=False),
    sa.Column('gearbox_type', sa.String(length=50), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cars_id'), 'cars', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cars_id'), table_name='cars')
    op.drop_table('cars')
    # ### end Alembic commands ###
