
-- Use the `ref` function to select from other models

select *
from {{ ref('speed_model') }}
where speed < 1.5
