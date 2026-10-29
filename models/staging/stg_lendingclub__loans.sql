with source as (

    select * from {{ source('lendingclub', 'loans') }}

),

cleaned as (

    select
        id as loan_id,
        try_cast(loan_amnt as double) as loan_amount,
        try_cast(funded_amnt as double) as funded_amount,
        try_cast(trim(replace(term, 'months', '')) as integer) as term_months,
        try_cast(replace(int_rate, '%', '') as double) as interest_rate,
        try_cast(installment as double) as installment,
        grade,
        sub_grade,
        home_ownership,
        try_cast(annual_inc as double) as annual_income,
        try_cast(dti as double) as debt_to_income,
        try_cast(fico_range_low as double) as fico_score,
        purpose,
        addr_state as state,
        cast(strptime(issue_d, '%b-%Y') as date) as issue_date,
        loan_status
    from source
    where loan_amnt is not null

)

select * from cleaned