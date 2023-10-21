/*
Enter your query here.
*/
select c.company_code,c.founder,
count(distinct lm.lead_manager_code) as Lead_managers,
count(distinct sm.senior_manager_code) as Senion_managers,
count(distinct m.manager_code) as Managers,
count(distinct e.employee_code) as Employees


from 
company c 
join Lead_Manager lm on lm.company_code = c.company_code
join Senior_Manager sm on sm.company_code = c.company_code 
join Manager m on m.company_code = c.company_code 
join Employee e on e.company_code = c.company_code

group by 1,2
order by 1;
