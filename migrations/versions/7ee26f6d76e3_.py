"""empty message

Revision ID: 7ee26f6d76e3
Revises: 597a80a7032a
Create Date: 2024-04-23 00:38:39.399964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee26f6d76e3'
down_revision = '597a80a7032a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('user_type', sa.String(length=50), nullable=True),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('user_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
