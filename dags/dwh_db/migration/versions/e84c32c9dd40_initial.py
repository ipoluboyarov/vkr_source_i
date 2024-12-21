"""initial

Revision ID: e84c32c9dd40
Revises: 
Create Date: 2024-12-18 02:02:38.733378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e84c32c9dd40'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dim_activity_code_main',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.668683', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('region_name', sa.String(length=255), nullable=True),
    sa.Column('area_name', sa.String(length=255), nullable=True),
    sa.Column('settlement_name', sa.String(length=255), nullable=True),
    sa.Column('settlement_type', sa.String(length=255), nullable=True),
    sa.Column('oktmo', sa.String(length=255), nullable=False),
    sa.Column('address_raw', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.671117', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_category_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.669506', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_data_confidence_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.667994', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_geo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lat', sa.String(length=255), nullable=False),
    sa.Column('lon', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.667212', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('short_name', sa.String(length=1000), nullable=False),
    sa.Column('reg_number', sa.String(length=255), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.670254', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dim_year',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.672702', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stg_empl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tin', sa.String(length=255), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('employees_count', sa.Integer(), nullable=True),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.666349', nullable=False),
    sa.Column('source', sa.String(length=50), server_default='empl.csv', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stg_revexp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tin', sa.String(length=255), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('revenue', sa.Float(), nullable=True),
    sa.Column('expenditure', sa.Float(), nullable=True),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.665363', nullable=False),
    sa.Column('source', sa.String(length=50), server_default='revexp.csv', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stg_smb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tin', sa.String(length=255), nullable=True),
    sa.Column('reg_number', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('org_name', sa.String(length=1000), nullable=True),
    sa.Column('org_short_name', sa.String(length=255), nullable=True),
    sa.Column('activity_code_main', sa.String(length=255), nullable=True),
    sa.Column('region', sa.String(length=255), nullable=True),
    sa.Column('area', sa.String(length=255), nullable=True),
    sa.Column('settlement', sa.String(length=255), nullable=True),
    sa.Column('settlement_type', sa.String(length=255), nullable=True),
    sa.Column('oktmo', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.String(length=255), nullable=True),
    sa.Column('lon', sa.String(length=255), nullable=True),
    sa.Column('address_raw', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.String(length=255), nullable=True),
    sa.Column('end_date', sa.String(length=255), nullable=True),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.662973', nullable=False),
    sa.Column('source', sa.String(length=50), server_default='smb.csv', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fact_smb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dim_organization_id', sa.Integer(), nullable=False),
    sa.Column('dim_category_type_id', sa.Integer(), nullable=False),
    sa.Column('dim_activity_code_main_id', sa.Integer(), nullable=False),
    sa.Column('dim_address_id', sa.Integer(), nullable=False),
    sa.Column('dim_geo_id', sa.Integer(), nullable=False),
    sa.Column('dim_year_id', sa.Integer(), nullable=False),
    sa.Column('dim_data_confidence_type_id', sa.Integer(), nullable=False),
    sa.Column('revenue', sa.Float(), nullable=False),
    sa.Column('expenditure', sa.Float(), nullable=False),
    sa.Column('employees_count', sa.Integer(), nullable=True),
    sa.Column('processed_at', sa.String(length=100), server_default='2024-12-18 02:02:38.673679', nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('last_stage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dim_activity_code_main_id'], ['dim_activity_code_main.id'], ),
    sa.ForeignKeyConstraint(['dim_address_id'], ['dim_address.id'], ),
    sa.ForeignKeyConstraint(['dim_category_type_id'], ['dim_category_type.id'], ),
    sa.ForeignKeyConstraint(['dim_data_confidence_type_id'], ['dim_data_confidence_type.id'], ),
    sa.ForeignKeyConstraint(['dim_geo_id'], ['dim_geo.id'], ),
    sa.ForeignKeyConstraint(['dim_organization_id'], ['dim_organization.id'], ),
    sa.ForeignKeyConstraint(['dim_year_id'], ['dim_year.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fact_smb')
    op.drop_table('stg_smb')
    op.drop_table('stg_revexp')
    op.drop_table('stg_empl')
    op.drop_table('dim_year')
    op.drop_table('dim_organization')
    op.drop_table('dim_geo')
    op.drop_table('dim_data_confidence_type')
    op.drop_table('dim_category_type')
    op.drop_table('dim_address')
    op.drop_table('dim_activity_code_main')
    # ### end Alembic commands ###