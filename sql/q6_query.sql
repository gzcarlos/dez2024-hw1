select a.lpep_dropoff_datetime, doff."Zone", a.tip_amount
from green_trips_data a
  join green_zones_data doff
    on a."DOLocationID" = doff."LocationID"
  join green_zones_data pup
    on a."PULocationID" = pup."LocationID"
where 
  -- filters for pickup
      a.lpep_pickup_datetime between '2019-09-01 00:00:00' and '2019-09-30 23:59:59'
  and pup."Zone" = 'Astoria'
order by a.tip_amount desc
LIMIT 1 -- remove to see all the data