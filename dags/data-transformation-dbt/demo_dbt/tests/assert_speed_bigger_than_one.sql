select 
    device_id,
    speed
from {{ ref('speed_model') }}
where speed < 1