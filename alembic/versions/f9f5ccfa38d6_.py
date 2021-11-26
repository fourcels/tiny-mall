"""empty message

Revision ID: f9f5ccfa38d6
Revises: 352368f77aae
Create Date: 2021-11-26 22:45:41.589202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f5ccfa38d6'
down_revision = '352368f77aae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'amount')
    # ### end Alembic commands ###
