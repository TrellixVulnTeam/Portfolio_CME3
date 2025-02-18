"""user

Revision ID: 9eca71f95e60
Revises: 0f343491696e
Create Date: 2020-05-10 11:19:53.325104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9eca71f95e60'
down_revision = '0f343491696e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('firstname', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('lastname', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(length=30), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    op.drop_column('users', 'lastname')
    op.drop_column('users', 'firstname')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
