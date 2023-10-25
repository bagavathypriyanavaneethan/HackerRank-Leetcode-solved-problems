/*
Enter your query here.
*/
select hacker_id,hacker_name as name
from 
(
select s.hacker_id,h.name as hacker_name,
count(distinct s.submission_id) as Sub_count

from 
submissions s 
join challenges c on s.challenge_id = c.challenge_id 
join difficulty d on d.difficulty_level = c.difficulty_level 
join hackers h on h.hacker_id = s.hacker_id

where d.score = s.score 

group by 1,2 having sub_count > 1 
) a 
order by sub_count desc,hacker_id 
