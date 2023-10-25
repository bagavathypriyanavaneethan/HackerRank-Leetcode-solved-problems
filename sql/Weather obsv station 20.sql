/*
Enter your query here.
*/

select round(LAT_N,4) 
from 
(select LAT_N,rank() over(order by LAT_N asc) as rnk from station) as t

where rnk= (select count(*) from station)/2
