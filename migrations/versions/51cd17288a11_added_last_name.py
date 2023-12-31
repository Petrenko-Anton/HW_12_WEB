"""added last_name

Revision ID: 51cd17288a11
Revises: 758c2117e952
Create Date: 2023-08-06 23:34:17.860788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51cd17288a11'
down_revision: Union[str, None] = '758c2117e952'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('last_name', sa.String(length=20), nullable=True))
    op.alter_column('contacts', 'description',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'description',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.drop_column('contacts', 'last_name')
    # ### end Alembic commands ###
