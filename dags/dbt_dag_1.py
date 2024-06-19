import os
from cosmos import DbtDag,ProjectConfig,ProfileConfig,ExecutionConfig
from datetime import datetime
from cosmos.profiles import PostgresUserPasswordProfileMapping

profile_config = ProfileConfig( 
     profile_name="default", 
     target_name="dev", 
     profile_mapping=PostgresUserPasswordProfileMapping( 
         conn_id="postgres", 
         profile_args={"schema": "k6"}, 
     ), 
 ) 
  

jaffle_shop = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/data-transformation-dbt/demo_dbt",),
	dag_id="postgre_dbt",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    
)

