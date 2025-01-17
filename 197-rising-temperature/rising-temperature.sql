# Write your MySQL query statement below
-- select c.id
-- from Weather c
-- where temperature > all (select temperature from Weather p where c.recordDate>p.recordDate)

select c.id
from Weather c
join Weather p
on c.recordDate=p.recordDate+ interval 1 day
where c.temperature > p.temperature;

-- select recordDate, recordDate- interval 1 day
-- from Weather
