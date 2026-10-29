from datetime import datetime
from pathlib import Path

from airflow.sdk import dag
from airflow.providers.standard.operators.bash import BashOperator
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig

PROJECT_DIR = Path("/Users/bhanu/lendlens")
DBT_EXECUTABLE = "/Users/bhanu/lendlens/.venv/bin/dbt"


@dag(
    start_date=datetime(2026, 1, 1),
    schedule="0 6 * * *",   # every day at 6 AM
    catchup=False,
    max_active_tasks=1,     # DuckDB allows only one writer at a time
)
def lendlens_pipeline():

    # Task 1: load FRED data with dlt (uses the dbt venv's Python)
    load_fred = BashOperator(
        task_id="load_fred_with_dlt",
        bash_command="cd /Users/bhanu/lendlens && .venv/bin/python fred_pipeline.py",
    )

    # Task 2: Cosmos turns every dbt model, seed, snapshot and test into its own task
    dbt_build = DbtTaskGroup(
        group_id="dbt",
        project_config=ProjectConfig(PROJECT_DIR),
        profile_config=ProfileConfig(
            profile_name="lendlens",
            target_name="dev",
            profiles_yml_filepath=PROJECT_DIR / "profiles.yml",
        ),
        execution_config=ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE),
    )

    load_fred >> dbt_build


lendlens_pipeline()