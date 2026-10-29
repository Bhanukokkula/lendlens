select
    observation_date as month_date,
    fedfunds as fed_funds_rate
from {{ source('fred', 'fedfunds') }}