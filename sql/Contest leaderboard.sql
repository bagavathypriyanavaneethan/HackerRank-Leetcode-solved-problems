/*
Enter your query here.
*/

select hacker_id,name,sum(score) as score

from 
(
    select h.hacker_id,h.name,challenge_id,max(score) as score

    from 
    Hackers h 
    join submissions s on h.hacker_id = s.hacker_id

    group by 1,2,3 
)der
group by 1,2 having score != 0
order by 3 desc,1
