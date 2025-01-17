# Write your MySQL query statement below
select 
    s.student_id, s.student_name, sub.subject_name,
    sum(case when e.subject_name is null then 0 else 1 end) as attended_exams
-- select *
from 
    (Students s join Subjects sub)
    left join Examinations e on s.student_id=e.student_id and sub.subject_name=e.subject_name

group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, sub.subject_name; 
