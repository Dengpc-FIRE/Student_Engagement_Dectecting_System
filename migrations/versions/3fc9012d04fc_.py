"""empty message

Revision ID: 3fc9012d04fc
Revises: 
Create Date: 2023-03-31 09:17:06.901474

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3fc9012d04fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_account_information',
    sa.Column('studentAccount', sa.String(length=100), nullable=False),
    sa.Column('studentPassword', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('studentAccount')
    )
    op.create_table('teacher_account_information',
    sa.Column('teacherAccount', sa.String(length=100), nullable=False),
    sa.Column('teacherPassword', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('teacherAccount')
    )
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               nullable=False)

    op.drop_table('teacher_account_information')
    op.drop_table('student_account_information')
    # ### end Alembic commands ###
