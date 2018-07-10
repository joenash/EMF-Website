"""Missing index/unique

Revision ID: c9968ce14aab
Revises: 45cafca4c9ef
Create Date: 2018-07-10 16:37:22.223621

"""

# revision identifiers, used by Alembic.
revision = 'c9968ce14aab'
down_revision = '45cafca4c9ef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_volunteer_venue_name'), 'volunteer_venue', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_volunteer_venue_name'), table_name='volunteer_venue')
    # ### end Alembic commands ###