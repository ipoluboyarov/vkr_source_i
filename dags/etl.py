import psycopg2

def load_empl_to_stage():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")  
    
    cur = conn.cursor()
    cur.execute('truncate table stg_empl')
    with open('source_data/empl.csv') as f:
        next(f)
        cur.copy_from(f, 'stg_empl', sep=';',columns=['tin','year','employees_count'])
    conn.commit()

def load_revexp_to_stage():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")   
    
    cur = conn.cursor()
    cur.execute('truncate table stg_revexp')
    with open('source_data/revexp.csv') as f:
        next(f)
        cur.copy_from(f, 'stg_revexp', sep=';',columns=['tin','year','revenue','expenditure'])
    conn.commit()

def load_smb_to_stage():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('truncate table stg_smb')
    with open('source_data/smb.csv') as f:
        next(f)
        cur.copy_from(f, 'stg_smb', sep=';',columns=['tin','reg_number','category','org_name','org_short_name','activity_code_main','region','area','settlement','settlement_type','oktmo','lat','lon','address_raw','start_date','end_date'])
    conn.commit()

def load_dim_activity_code_main_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_activity_code_main();')
    conn.commit()

def load_dim_address_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_address();')
    conn.commit()

def load_dim_category_type_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_category_type();')
    conn.commit()

def load_dim_geo_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_geo();')
    conn.commit()

def load_dim_organization_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_organization();')
    conn.commit()

def load_dim_year_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_dim_year();')
    conn.commit()

def load_fact_smb_to_dwh():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_load_fact_smb();')
    conn.commit()

def proc_send_stage_statistic():
    conn = psycopg2.connect("host=vkr_source-postgres-1 dbname=dwh_db user=airflow password=airflow")
    
    cur = conn.cursor()
    cur.execute('CALL proc_send_stage_statistic();')
    conn.commit()

