"""empty message

Revision ID: 21125409639d
Revises: 32f7fd8ac173
Create Date: 2019-05-21 02:56:50.903974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '21125409639d'
down_revision = '32f7fd8ac173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_dataa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('macaddress', sa.String(length=80), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('frequency', sa.Integer(), nullable=True),
    sa.Column('rssi', sa.Integer(), nullable=True),
    sa.Column('scantime', sa.String(length=80), nullable=True),
    sa.Column('percentage', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('history_dataa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(length=80), nullable=True),
    sa.Column('xcords', sa.Float(), nullable=True),
    sa.Column('ycords', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_dataa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_devicess',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('devicename', sa.String(length=80), nullable=True),
    sa.Column('macaddress', sa.String(length=80), nullable=True),
    sa.Column('longg', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_devices')
    op.drop_table('app_data')
    op.drop_table('test_data')
    op.drop_table('history_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('time', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('xcords', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('ycords', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'history_data_pkey')
    )
    op.create_table('test_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'test_data_pkey')
    )
    op.create_table('app_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('distance', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('frequency', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('scantime', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('macaddress', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('rssi', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('percentage', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'app_data_pkey')
    )
    op.create_table('user_devices',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('devicename', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('macaddress', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('longg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('lat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_devices_pkey')
    )
    op.drop_table('user_devicess')
    op.drop_table('test_dataa')
    op.drop_table('history_dataa')
    op.drop_table('app_dataa')
    # ### end Alembic commands ###
