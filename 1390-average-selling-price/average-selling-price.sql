# Write your MySQL query statement below
-- select
--     *
--     -- p.product_id
--     -- sum(p.price)*u.units/u.units average_price
-- from Prices p
-- join UnitsSold u
-- on p.product_id=u.product_id and u.purchase_date between p.start_date and p.end_date
-- group by p.product_id; 

with up as(
    select product_id, round(sum(cost)/sum(units),2) as average_price
    from (
        select u.product_id, u.units, u.units*p.price as cost
        from UnitsSold u
        left join Prices p
        on u.product_id=p.product_id
        where u.purchase_date between p.start_date and p.end_date
    ) as pp
    group by product_id
),
cp as (
    select distinct product_id
    from Prices
)
select cp.product_id, coalesce(up.average_price,0) as average_price
from cp
left join up
on cp.product_id=up.product_id
-- select p.product_id
-- from Prices p
-- left join up
-- on p.product_id=up.product_id
-- group by p.product_id;