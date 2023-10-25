/*
Enter your query here.
*/

select case when g.grade < 8 then null else s.name end as name,
grade,marks

from 
students s 
join grades g on s.marks between g.min_mark and g.max_mark 

order by g.grade desc,case when g.grade between 8 and 10 then name
else marks end
