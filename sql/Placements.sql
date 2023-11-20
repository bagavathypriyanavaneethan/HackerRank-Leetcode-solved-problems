/*
Enter your query here.
*/
select name
from 
(
select s.name as name,sp.salary,sf.salary as friend_salary

from 
students s
join friends f on s.id = f.id 
join packages sp on sp.id = s.id 
join packages sf on sf.id = f.friend_id

where sf.salary > sp.salary
)a
order by friend_salary
