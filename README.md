# DataTalks.club - Data Engineering Zoomcamp 2024 homework#1

### Setup

1. Install terraform with this commands

    ```bash
    wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install terraform
    ```
2. instal Jupyter Notebook using `pip` and other packages like `sqlachemy`, `psycopg2` and `argparse`
    ```bash
    pip install jupyter sqlachemy psycopg2 argparse
    ```
    In case you want to test it run this command on your `terminal`
    ```bash
    jupyter notebook
    ```
3. Prepare Docker components
    <br>
    **Create Network**
    ```bash
    docker network create pg-network
    ```

    **Create Volume**
    ```bash
    docker volume create --name dtc_postgres_volume_local -d local
    ```

### Run Postgres DB engine on Docker
1. Excute this command on `terminal`
```bash
docker run -it \
-e POSTGRES_USER="root" \ 
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="taxi_db" \
-v dtc_postgres_volume_local:/var/lib/postgressql/data \
-p 5432:5432 \
--network pg-network \
--name pg-database \
postgres:13
```

2. Execute this on aother `terminal`
```bash
docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network pg-network \
--name pdadmin \
dpage/pgadmin4
```

### Convert Jupyter Notebook to `.py` script

```bash
jupyter nbconvert --to=script upload_data.ipynb
```

## Homework Submission

For homework #1 submission the queries for the green taxi trips related questions (Q's) are as follows

#### Q3 - How many taxi trips were totally made on September 18th 2019?

```sql
select count(*) from green_trips_data a
where a.lpep_pickup_datetime between '2019-09-18' and '2019-09-18 23:59:59'
  and a.lpep_dropoff_datetime between '2019-09-18' and '2019-09-18 23:59:59'
```

#### Q4 - Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

```sql
select 
    date_trunc('day', a.lpep_pickup_datetime) lpep_pickup_datetime
  , max(a.trip_distance) max_trip_distance
from green_trips_data a
group by date_trunc('day', a.lpep_pickup_datetime)
order by max_trip_distance desc
LIMIT 1 -- remote to see all the data
```

#### Q5 - Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

```sql
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
```
#### Q6 - For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?

```sql
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
```

#### Q7 - Creating Resources

Perform this commands in the exact order

```bash
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=dez-2024"
```

Then execute the `apply` and this whole output paste it in the Question 7 input field

```bash
# Create new infra
terraform apply -var="project=dez-2024"
```

Finally execute the `destroy`

```bash
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```

