/*
Enter your query here.
*/
with result as 
(
    select city,
    char_length(city) as length,
    row_number()over(order by char_length(city),city) as min,
    row_number()over(order by char_length(city) desc,city) as max
    
    from 
    station 
)

(select city,length from result where min = 1)
union all 
(select city,length from result where max = 1)
