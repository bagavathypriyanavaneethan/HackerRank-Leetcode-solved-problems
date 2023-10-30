/*
Enter your query here.
*/

set @project_id = 1;

with project_info as 
(
    select *,
    case when days <= 1 then @project_id := @project_id
    else @project_id := @project_id +1 end as project_id 
    from 
    (
        select *,coalesce(lag(end_date)over(order by end_date),end_date) as previous_end_day,
        datediff(end_date,coalesce(lag(end_date)over(order by end_date),end_date)) as days

        from 
        projects
    ) proj
)

select min(start_date) as start_date,max(end_date) as end_date
from 
(
select * 
from 
project_info
) inf
group by project_id 
order by max(end_date) - min(start_date),min(start_date)
