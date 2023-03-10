"""up table

Revision ID: 508ad142f11e
Revises: de1b81f7cc37
Create Date: 2023-03-04 20:47:05.273231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '508ad142f11e'
down_revision = 'de1b81f7cc37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livestock', schema=None) as batch_op:
        batch_op.add_column(sa.Column('classifications', sa.String(length=64), nullable=False))
        batch_op.drop_constraint('livestock_classification_key', type_='unique')
        batch_op.create_unique_constraint(None, ['classifications'])
        batch_op.drop_column('classification')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livestock', schema=None) as batch_op:
        batch_op.add_column(sa.Column('classification', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('livestock_classification_key', ['classification'])
        batch_op.drop_column('classifications')

    # ### end Alembic commands ###
