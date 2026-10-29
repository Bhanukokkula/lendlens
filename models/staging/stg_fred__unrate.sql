select
    cast(observation_date as date) as month_date,
    try_cast(unrate as double) as unemployment_rate
from {{ source('fred', 'unrate') }}