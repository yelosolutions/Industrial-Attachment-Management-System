"""new

Revision ID: 4f8f28b8cb00
Revises: 11ac6fbc6c3a
Create Date: 2022-11-16 21:57:33.157753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8f28b8cb00'
down_revision = '11ac6fbc6c3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('contact', sa.String(length=128), nullable=True),
    sa.Column('period', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_application_email'), 'application', ['email'], unique=True)
    op.create_index(op.f('ix_application_studentname'), 'application', ['studentname'], unique=True)
    op.drop_index('ix_request_email', table_name='request')
    op.drop_index('ix_request_studentname', table_name='request')
    op.drop_table('request')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('request_id', sa.INTEGER(), nullable=False),
    sa.Column('studentname', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('contact', sa.VARCHAR(length=128), nullable=True),
    sa.Column('period', sa.DATE(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('request_id')
    )
    op.create_index('ix_request_studentname', 'request', ['studentname'], unique=False)
    op.create_index('ix_request_email', 'request', ['email'], unique=False)
    op.drop_index(op.f('ix_application_studentname'), table_name='application')
    op.drop_index(op.f('ix_application_email'), table_name='application')
    op.drop_table('application')
    # ### end Alembic commands ###
