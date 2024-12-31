
"""Added video beignning and end points

Revision ID: ba6827b08085
Revises: b49d8b2a763f
Create Date: 2024-12-30 17:03:13.161673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba6827b08085'
down_revision = 'b49d8b2a763f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('video_start', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('video_end', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.drop_column('video_end')
        batch_op.drop_column('video_start')

    # ### end Alembic commands ###
