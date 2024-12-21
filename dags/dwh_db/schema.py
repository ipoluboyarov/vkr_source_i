from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from datetime import datetime, date
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://airflow:airflow@vkr_source-postgres-1/dwh_db')

Base = declarative_base()

class stg_smb(Base):
    __tablename__ = "stg_smb"
    id = Column(Integer, primary_key=True)
    tin = Column(String(255), nullable=True)
    reg_number = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    org_name = Column(String(1000), nullable=True)
    org_short_name = Column(String(255), nullable=True)
    activity_code_main = Column(String(255), nullable=True)
    region = Column(String(255), nullable=True)
    area = Column(String(255), nullable=True)
    settlement = Column(String(255), nullable=True)
    settlement_type = Column(String(255), nullable=True)
    oktmo = Column(String(255), nullable=True)
    lat = Column(String(255), nullable=True)
    lon = Column(String(255), nullable=True)
    address_raw = Column(String(255), nullable=True)
    start_date = Column(String(255), nullable=True)
    end_date = Column(String(255), nullable=True)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False, server_default = 'smb.csv')


class stg_revexp(Base):
    __tablename__ = "stg_revexp"
    id = Column(Integer, primary_key=True)
    tin = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    revenue = Column(Float, nullable=True)
    expenditure = Column(Float, nullable=True)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False, server_default = 'revexp.csv')

class stg_empl(Base):
    __tablename__ = "stg_empl"
    id = Column(Integer, primary_key=True)
    tin = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    employees_count = Column(Integer, nullable=True)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False, server_default = 'empl.csv')

class dim_geo(Base):
    __tablename__ = "dim_geo"
    id = Column(Integer, primary_key=True)
    lat = Column(String(255), nullable=False)
    lon = Column(String(255), nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class dim_activity_code_main(Base):
    __tablename__ = "dim_activity_code_main"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class dim_category_type(Base):
    __tablename__ = "dim_category_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class dim_organization(Base):
    __tablename__ = "dim_organization"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    short_name = Column(String(1000), nullable=False)
    reg_number = Column(String(255), nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class dim_address(Base):
    __tablename__ = "dim_address"
    id = Column(Integer, primary_key=True)
    region_name = Column(String(255), nullable=True)
    area_name = Column(String(255), nullable=True)
    settlement_name = Column(String(255), nullable=True)
    settlement_type = Column(String(255), nullable=True)
    oktmo = Column(String(255), nullable=False)
    address_raw = Column(String(255), nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class dim_year(Base):
    __tablename__ = "dim_year"
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)

class fact_smb(Base):
    __tablename__ = "fact_smb"
    id = Column(Integer, primary_key=True)
    dim_organization_id = Column(Integer, ForeignKey('dim_organization.id'), nullable=False)
    dim_category_type_id = Column(Integer, ForeignKey('dim_category_type.id'), nullable=False)
    dim_activity_code_main_id = Column(Integer, ForeignKey('dim_activity_code_main.id'), nullable=False)
    dim_address_id = Column(Integer, ForeignKey('dim_address.id'), nullable=False)
    dim_geo_id = Column(Integer, ForeignKey('dim_geo.id'), nullable=False)
    dim_year_id = Column(Integer, ForeignKey('dim_year.id'), nullable=False)
    dim_data_confidence_type_id = Column(Integer, ForeignKey('dim_data_confidence_type.id'), nullable=False)
    revenue = Column(Float, nullable=False)
    expenditure = Column(Float, nullable=False)
    employees_count = Column(Integer, nullable=True)
    processed_at = Column(String(100), nullable=False, server_default = str(datetime.now()))
    source = Column(String(50), nullable=False)
    last_stage_id = Column(Integer, nullable=False)
   






