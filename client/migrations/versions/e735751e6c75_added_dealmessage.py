"""Added DealMessage

Revision ID: e735751e6c75
Revises: 9e8756f3ba69
Create Date: 2018-08-11 12:03:11.312022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e735751e6c75'
down_revision = '9e8756f3ba69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deal_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deal_message_contract_id'), 'deal_message', ['contract_id'], unique=False)
    op.create_index(op.f('ix_deal_message_user_id'), 'deal_message', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_deal_message_user_id'), table_name='deal_message')
    op.drop_index(op.f('ix_deal_message_contract_id'), table_name='deal_message')
    op.drop_table('deal_message')
    # ### end Alembic commands ###
