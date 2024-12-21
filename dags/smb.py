import pendulum

from etl import load_empl_to_stage, load_revexp_to_stage, load_smb_to_stage
from etl import load_dim_activity_code_main_to_dwh, load_dim_address_to_dwh, load_dim_category_type_to_dwh, load_dim_geo_to_dwh, load_dim_organization_to_dwh, load_dim_year_to_dwh
from etl import load_fact_smb_to_dwh,proc_send_stage_statistic

from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator


@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 9, tz="UTC"),
    catchup=False,
    template_searchpath='out/stage/sql/',
    tags=["example"]
)
def smb():

    load_empl_to_stage_task = PythonOperator(
        task_id="load_empl_to_stage",
        python_callable=load_empl_to_stage
    )

    load_revexp_to_stage_task = PythonOperator(
        task_id="load_revexp_to_stage",
        python_callable=load_revexp_to_stage
    )

    load_smb_to_stage_task = PythonOperator(
        task_id="load_smb_to_stage",
        python_callable=load_smb_to_stage
    )

    load_dim_activity_code_main_to_dwh_task = PythonOperator(
        task_id="load_dim_activity_code_main_to_dwh",
        python_callable=load_dim_activity_code_main_to_dwh
    )

    load_dim_address_to_dwh_task = PythonOperator(
        task_id="load_dim_address_to_dwh",
        python_callable=load_dim_address_to_dwh
    )

    load_dim_category_type_to_dwh_task = PythonOperator(
        task_id="load_dim_category_type_to_dwh",
        python_callable=load_dim_category_type_to_dwh
    )

    load_dim_geo_to_dwh_task = PythonOperator(
        task_id="load_dim_geo_to_dwh",
        python_callable=load_dim_geo_to_dwh
    )

    load_dim_organization_to_dwh_task = PythonOperator(
        task_id="load_dim_organization_to_dwh",
        python_callable=load_dim_organization_to_dwh
    )

    load_dim_year_to_dwh_task = PythonOperator(
        task_id="load_dim_year_to_dwh",
        python_callable=load_dim_year_to_dwh
    )

    load_fact_smb_to_dwh_task = PythonOperator(
        task_id="load_fact_smb_to_dwh",
        python_callable=load_fact_smb_to_dwh
    )

    proc_send_stage_statistic_task = PythonOperator(
        task_id="proc_send_stage_statistic",
        python_callable=proc_send_stage_statistic
    )

    [load_empl_to_stage_task , load_revexp_to_stage_task , load_smb_to_stage_task] >> proc_send_stage_statistic_task >>  [load_dim_activity_code_main_to_dwh_task,load_dim_address_to_dwh_task,load_dim_category_type_to_dwh_task,load_dim_geo_to_dwh_task,load_dim_organization_to_dwh_task,load_dim_year_to_dwh_task] >> load_fact_smb_to_dwh_task


smb()