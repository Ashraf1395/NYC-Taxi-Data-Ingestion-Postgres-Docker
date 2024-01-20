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
