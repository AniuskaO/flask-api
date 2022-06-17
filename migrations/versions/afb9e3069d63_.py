"""empty message

Revision ID: afb9e3069d63
Revises: ecab8d135a62
Create Date: 2022-06-16 23:06:13.040530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb9e3069d63'
down_revision = 'ecab8d135a62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Donacion',
    sa.Column('id_donacion', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_donacion')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Donacion')
    # ### end Alembic commands ###
