-- Default rate by issue year and grade, using only finished loans
select
    year(issue_date) as vintage_year,
    grade,
    count(*) as loan_count,
    sum(funded_amount) as total_funded,
    round(avg(interest_rate), 2) as avg_interest_rate,
    round(avg(is_default) * 100, 2) as default_rate_pct
from {{ ref('fct_loans') }}
where loan_status like '%Fully Paid'
   or loan_status like '%Charged Off'
   or loan_status = 'Default'
group by 1, 2
order by 1, 2