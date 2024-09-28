"""empty message

Revision ID: db06bde05653
Revises: 
Create Date: 2024-09-27 19:47:16.327342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db06bde05653'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video',
    sa.Column('video_id', sa.String(length=36), nullable=False),
    sa.Column('character_name', sa.String(length=50), nullable=False),
    sa.Column('video_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('video_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video')
    # ### end Alembic commands ###
