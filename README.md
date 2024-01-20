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


Creating a pgadmin container

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="ashraf@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="ashraf" \
    -p 8080:80 \
    --network=postgres-network \
    --name=pg-admin \
    dpage/pgadmin4


Create network

docker network create postgres-network

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="ashraf" \
  -e POSTGRES_DB="nyc_taxi" \
  -v c:/Users/DELL/Desktop/projects/NYC-Taxi-Data-Ingestion-Postgres-Docker/postgres_data:/var/lib/postgressql/data \
  -p 5432:5432 \
  --network=postgres-network \
  --name pg-database \
  postgres:13
