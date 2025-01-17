# Write your MySQL query statement below

with
aC as (
    select user_id, count(action) as confirmed
    from Confirmations
    where action='confirmed'
    group by user_id
),
T as (
    select user_id, count(action) as total
    from Confirmations
    group by user_id
)
select
    s.user_id,
    round(
        case
        when T.total is null or aC.confirmed is null then 0
        else aC.confirmed/T.total
        end,
    2) as confirmation_rate
from Signups s
left join aC
on s.user_id=aC.user_id
left join T
on s.user_id=T.user_id;