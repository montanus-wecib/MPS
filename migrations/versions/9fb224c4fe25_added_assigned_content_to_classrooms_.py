"""Added assigned_content to classrooms table

Revision ID: 9fb224c4fe25
Revises: 06db76eab812
Create Date: 2025-01-22 16:21:13.841401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fb224c4fe25'
down_revision = '06db76eab812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('classroom', schema=None) as batch_op:
        batch_op.add_column(sa.Column('assigned_content', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('classroom', schema=None) as batch_op:
        batch_op.drop_column('assigned_content')

    # ### end Alembic commands ###
