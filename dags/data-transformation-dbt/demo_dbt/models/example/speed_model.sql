

{{ config(materialized='view') }}

{% set table_columns = ["device_id", "speed"] %}

with source_data as (
    select index,updated_at,device_id,{{increase_one('speed')}} as speed
    from devices
)

select *
from source_data
