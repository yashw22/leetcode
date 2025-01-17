# Write your MySQL query statement below

with
c as (
    select
        user_id,
        count(action) as total,
        count(case when action='confirmed' then 1 end) as confirmed
    from Confirmations
    group by user_id
)
select
    s.user_id,
    round( coalesce(c.confirmed,0)/coalesce(c.total,1), 2) as confirmation_rate
from Signups s
left join c
on s.user_id=c.user_id;