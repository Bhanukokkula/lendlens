{{ config(
    materialized = 'incremental',
    unique_key = 'issue_month'
) }}

select
    issue_date as issue_month,
    count(*) as loans_issued,
    sum(funded_amount) as total_funded,
    round(avg(interest_rate), 2) as avg_interest_rate,
    max(fed_funds_rate) as fed_funds_rate
from {{ ref('fct_loans') }}
where issue_date <= '{{ var("load_until", "2099-12-01") }}'

{% if is_incremental() %}
    -- only months newer than what's already in the table
    and issue_date > (select max(issue_month) from {{ this }})
{% endif %}

group by 1