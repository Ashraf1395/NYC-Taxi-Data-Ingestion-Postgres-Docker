# NYC-Taxi-Data-Ingestion-Postgres-Docker

Docker command to run postgress in a container 
v stands for volume
p for port

  docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="ashraf" \
  -e POSTGRES_DB="nyc_taxi" \
  -v c:/Users/DELL/Desktop/projects/NYC-Taxi-Data-Ingestion-Postgres-Docker/postgres_data:/var/lib/postgressql/data \
  -p 5432 \
  postgres:13

Using pgcli

pip install pgcli
pgcli -h localhost -p 5432 -d nyc_taxi

pip install psycopg2-binary

Using psql
$ docker exec -it CONTAINER_ID psql -U root -d nyc_taxi


Creating schema statement
pg.io.sql.get_schema(df,'green_taxi_data')


Create network

docker network create postgres-network

Running postgres

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="ashraf" \
  -e POSTGRES_DB="nyc_taxi" \
  -v c:/Users/DELL/Desktop/projects/NYC-Taxi-Data-Ingestion-Postgres-Docker/postgres_data:/var/lib/postgressql/data \
  -p 5432:5432 \
  --network=postgres-network \
  --name pg-database \
  postgres:13

Creating a pgadmin container

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="ashraf@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="ashraf" \
    -p 8080:80 \
    --network=postgres-network \
    --name=pg-admin \
    dpage/pgadmin4

Running the pipe.py file with arguments
  python pipe.py \
    --user=root \
    --password=ashraf \
    --host=localhost \
    --db=nyc_taxi \
    --table_name=green_taxi_data

Creating docker image for the Dockerfile

docker build -t taxi_data_ingestion:v001 .

docker run -it \
    --network=postgres-network \
    --name=ingestion_pipeline \
    taxi_data_ingestion:v002 \
        --user=root \
        --password=ashraf \
        --host=pgdatabase \
        --db=nyc_taxi \
        --table_name=green_taxi_data
    

Running Docker Compose file

docker-compose up

In detached mode (get your terminal back)
docker-compose up -d

Stop the container
docker-compose down