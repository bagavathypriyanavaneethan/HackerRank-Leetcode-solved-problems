# Write your MySQL query statement below

select name 

from 
SalesPerson sp 

left join 
(
    select sales_id 
    from 
    orders ord 
    join company cmp on ord.com_id = cmp.com_id 
    and cmp.name = 'RED'
) red on red.sales_id = sp.sales_id 

where red.sales_id is null 
