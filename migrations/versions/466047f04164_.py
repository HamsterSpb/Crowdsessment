"""empty message

Revision ID: 466047f04164
Revises: 45f8c0fec7b0
Create Date: 2019-02-25 02:01:09.302984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466047f04164'
down_revision = '45f8c0fec7b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check', sa.Column('checks_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('check', 'checks_count')
    # ### end Alembic commands ###
