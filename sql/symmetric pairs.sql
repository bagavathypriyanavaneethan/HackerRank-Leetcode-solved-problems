/*
Enter your query here.
*/
-- To remove the self join  eg x1 = 1 and x2 = 1 
with a_rnk as 
(
    select *,row_number()over() as rnk
    
    from 
    functions 
)
select * 
from 
(
select case when least(a.x,b.x) = a.x then a.x else b.x end as x,
case when least(a.x,b.x) = a.x then a.y else b.y end as y

from 
a_rnk a 
join a_rnk b on a.x = b.y 
and a.y = b.x 
and a.rnk != b.rnk 
    
group by 1,2
) der
order by 1
