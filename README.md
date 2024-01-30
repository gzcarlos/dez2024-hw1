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

