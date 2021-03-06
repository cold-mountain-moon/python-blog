"""empty message

Revision ID: cdea1d498992
Revises: b043ef722d4d
Create Date: 2018-09-20 14:09:40.279943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdea1d498992'
down_revision = 'b043ef722d4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_tag',
    sa.Column('articleid', sa.Integer(), nullable=False),
    sa.Column('tagid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['articleid'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tagid'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('articleid', 'tagid')
    )
    op.add_column('catogory', sa.Column('route', sa.String(length=127), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('catogory', 'route')
    op.drop_table('article_tag')
    # ### end Alembic commands ###
