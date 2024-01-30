select 
    date_trunc('day', a.lpep_pickup_datetime) lpep_pickup_datetime
  , max(a.trip_distance) max_trip_distance
from green_trips_data a
group by date_trunc('day', a.lpep_pickup_datetime)
order by max_trip_distance desc
LIMIT 1 -- remote to see all the data