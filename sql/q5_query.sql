-- this question does no consider the top 3, even there are more than 3 Borough that have more than 50000 on sum of total_amount
select  b."Borough", sum(a.total_amount) as sum_total_amount
from green_trips_data a
  join green_zones_data b
    on a."PULocationID" = b."LocationID"
where a.lpep_pickup_datetime between '2019-09-18' and '2019-09-18 23:59:59'
  and b."Borough" != 'Unknown'
group by b."Borough"
having sum(a.total_amount) >= 50000
order by sum_total_amount desc
LIMIT 3 -- remote to see all the data