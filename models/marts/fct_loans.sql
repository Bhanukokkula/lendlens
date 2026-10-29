with loans as (

    select * from {{ ref('int_loans_enriched') }}

),

grades as (

    select * from {{ ref('grade_risk_buckets') }}

)

select
    loans.loan_id,
    loans.issue_date,
    loans.grade,
    grades.risk_bucket,
    loans.state,
    loans.purpose,
    loans.term_months,
    loans.loan_amount,
    loans.funded_amount,
    loans.interest_rate,
    loans.fed_funds_rate,
    loans.unemployment_rate,
    loans.rate_spread,
    loans.annual_income,
    loans.debt_to_income,
    loans.fico_score,
    loans.loan_status,
    loans.is_default
from loans
left join grades
    on loans.grade = grades.grade