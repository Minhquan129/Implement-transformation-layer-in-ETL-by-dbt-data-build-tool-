FROM quay.io/astronomer/astro-runtime:11.3.0
USER root
RUN sudo apt-get update
RUN sudo apt-get install libpq-dev -y
WORKDIR "/usr/local/airflow"
COPY dbt-requirements.txt ./
RUN python -m virtualenv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir -r dbt-requirements.txt && deactivate
