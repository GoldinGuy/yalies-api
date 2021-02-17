"""rename users to user

Revision ID: e5cd54c27428
Revises: d315b6c24d70
Create Date: 2021-02-16 20:35:14.722357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5cd54c27428'
down_revision = 'd315b6c24d70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    """
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('registered_on', sa.Integer(), nullable=True),
    sa.Column('last_seen', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    """
    op.drop_constraint('key_user_id_fkey', 'key', type_='foreignkey')
    op.rename_table('users', 'user')
    op.create_foreign_key('key_user_id_fkey', 'key', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    pass