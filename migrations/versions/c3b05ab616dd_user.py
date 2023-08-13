"""User

Revision ID: c3b05ab616dd
Revises: f23fe9f3cc94
Create Date: 2023-08-12 21:27:18.065788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3b05ab616dd'
down_revision: Union[str, None] = 'f23fe9f3cc94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('refresh_token', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'refresh_token')
    # ### end Alembic commands ###
