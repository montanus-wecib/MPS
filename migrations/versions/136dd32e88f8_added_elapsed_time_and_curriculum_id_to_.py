
"""added elapsed_time and curriculum_id to XP table

Revision ID: 136dd32e88f8
Revises: 61a35d12c856
Create Date: 2025-01-04 12:27:36.177459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '136dd32e88f8'
down_revision = '61a35d12c856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xp', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curriculum_id', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('elapsed_time', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xp', schema=None) as batch_op:
        batch_op.drop_column('elapsed_time')
        batch_op.drop_column('curriculum_id')

    # ### end Alembic commands ###
