"""empty message

Revision ID: 85344d862fa9
Revises: fad4050af408
Create Date: 2021-01-19 01:24:55.237959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85344d862fa9'
down_revision = 'fad4050af408'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###
