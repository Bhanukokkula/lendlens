select
    observation_date as month_date,
    unrate as unemployment_rate
from {{ source('fred', 'unrate') }}