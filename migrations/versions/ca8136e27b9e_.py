"""empty message

Revision ID: ca8136e27b9e
Revises: ad1bb4c36dad
Create Date: 2018-07-26 11:36:05.750048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca8136e27b9e'
down_revision = 'ad1bb4c36dad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('cid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('qid', sa.Integer(), nullable=True),
    sa.Column('aid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aid'], ['user.uid'], ),
    sa.ForeignKeyConstraint(['qid'], ['question.qid'], ),
    sa.PrimaryKeyConstraint('cid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
