-- Fails if any loan has an unrealistic interest rate
select *
from {{ ref('stg_lendingclub__loans') }}
where interest_rate < 0
   or interest_rate > 40