"""empty message

Revision ID: a66134bb83a6
Revises: 2a420e8ebb72
Create Date: 2022-06-16 21:34:02.981263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a66134bb83a6'
down_revision = '2a420e8ebb72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Descuento_Producto',
    sa.Column('descuento_producto_id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('descuento_id', sa.Integer(), nullable=False),
    sa.Column('fecha_incio', sa.Integer(), nullable=False),
    sa.Column('fecha_termino', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('descuento_producto_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Descuento_Producto')
    # ### end Alembic commands ###
