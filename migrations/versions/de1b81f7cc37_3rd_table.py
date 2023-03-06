"""3rd table

Revision ID: de1b81f7cc37
Revises: c3f9908f027e
Create Date: 2023-03-04 20:01:03.424670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de1b81f7cc37'
down_revision = 'c3f9908f027e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('livestock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(length=64), nullable=False),
    sa.Column('species', sa.String(length=64), nullable=False),
    sa.Column('breed', sa.String(length=64), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('breed'),
    sa.UniqueConstraint('classification'),
    sa.UniqueConstraint('species')
    )
    op.create_table('collected_animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('livestock_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['livestock_id'], ['livestock.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('animal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('classification', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('species', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('breed', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('amount', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='animal_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='animal_pkey'),
    sa.UniqueConstraint('amount', name='animal_amount_key'),
    sa.UniqueConstraint('breed', name='animal_breed_key'),
    sa.UniqueConstraint('classification', name='animal_classification_key'),
    sa.UniqueConstraint('species', name='animal_species_key')
    )
    op.drop_table('collected_animals')
    op.drop_table('livestock')
    # ### end Alembic commands ###