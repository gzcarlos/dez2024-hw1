select count(*) from green_trips_data a
where a.lpep_pickup_datetime between '2019-09-18' and '2019-09-18 23:59:59'
  and a.lpep_dropoff_datetime between '2019-09-18' and '2019-09-18 23:59:59'