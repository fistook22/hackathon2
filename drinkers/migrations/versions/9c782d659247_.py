"""empty message

Revision ID: 9c782d659247
Revises: 
Create Date: 2022-01-12 20:32:57.340832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c782d659247'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drinker',
    sa.Column('drinker_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('gender', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('drinker_id')
    )
    op.create_table('the_drink',
    sa.Column('drink_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('distillery', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('color', sa.String(length=32), nullable=True),
    sa.Column('finish', sa.String(length=32), nullable=True),
    sa.Column('drinker', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['drinker'], ['drinker.drinker_id'], ),
    sa.PrimaryKeyConstraint('drink_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('the_drink')
    op.drop_table('drinker')
    # ### end Alembic commands ###
