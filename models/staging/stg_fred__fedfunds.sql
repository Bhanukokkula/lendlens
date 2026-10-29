
select
    cast(observation_date as date) as month_date,
    try_cast(fedfunds as double) as fed_funds_rate
from {{ source('fred', 'fedfunds') }}