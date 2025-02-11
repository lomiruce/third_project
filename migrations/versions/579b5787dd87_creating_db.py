"""creating db

Revision ID: 579b5787dd87
Revises: 
Create Date: 2024-09-26 16:15:20.217566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579b5787dd87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gamepicture', sa.String(length=150), nullable=True),
    sa.Column('gamename', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=800), nullable=False),
    sa.Column('developer', sa.String(length=100), nullable=False),
    sa.Column('publisher', sa.String(length=100), nullable=False),
    sa.Column('releasedate', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('commentid', sa.Integer(), nullable=False),
    sa.Column('commentatorsname', sa.String(length=80), nullable=False),
    sa.Column('comment', sa.String(length=800), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('commentid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('game')
    # ### end Alembic commands ###
