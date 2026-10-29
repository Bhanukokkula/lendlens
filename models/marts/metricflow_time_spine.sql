{{ config(materialized = 'table') }}

select cast(range as date) as date_day
from range(timestamp '2000-01-01', timestamp '2030-01-01', interval 1 day)