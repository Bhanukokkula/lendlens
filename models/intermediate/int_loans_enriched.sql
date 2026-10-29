with loans as (

    select * from {{ ref('stg_lendingclub__loans') }}

),

fedfunds as (

    select * from {{ ref('stg_fred__fedfunds') }}

),

unrate as (

    select * from {{ ref('stg_fred__unrate') }}

),

joined as (

    select
        loans.*,
        fedfunds.fed_funds_rate,
        unrate.unemployment_rate,
        loans.interest_rate - fedfunds.fed_funds_rate as rate_spread,
        case
            when loans.loan_status = 'Charged Off' then 1
            when loans.loan_status = 'Default' then 1
            when loans.loan_status = 'Does not meet the credit policy. Status:Charged Off' then 1
            else 0
        end as is_default
    from loans
    left join fedfunds
        on loans.issue_date = fedfunds.month_date
    left join unrate
        on loans.issue_date = unrate.month_date

)

select * from joined