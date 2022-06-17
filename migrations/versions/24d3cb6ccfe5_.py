"""empty message

Revision ID: 24d3cb6ccfe5
Revises: 0cf39328d9c2
Create Date: 2022-06-16 22:09:37.483822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24d3cb6ccfe5'
down_revision = '0cf39328d9c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comuna',
    sa.Column('id_comuna', sa.Integer(), nullable=False),
    sa.Column('nombre_comuna', sa.String(length=250), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_comuna')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Comuna')
    # ### end Alembic commands ###
