"""add review

Revision ID: 297b48f44b27
Revises: 103137724651
Create Date: 2024-04-04 13:58:11.897497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '297b48f44b27'
down_revision = '103137724651'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('column_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['column_id'], ['items.id'], name=op.f('fk_reviews_column_id_items')),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_reviews_customer_id_customers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
