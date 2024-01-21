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
    --table_name=taxi_lookup_data

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

Install terraform 

Install the terraform binary file
Add it to your system path

export PATH=$PATH:/path/to/terraform

Check it 
terraform --version

Initialise terraform

teerraform init

Your Architecture setup

terraform plan

Deploying 

terraform apply

Delete


terrafrom destroy

Answer
-1 -rm
-2 0.42.0
-3 15612
-4 2019-09-26
-5 Brooklyn-Manhattan-Queens
-6 JFK Airport
Query for Ques 3 : select count(*) from "green_taxi_data_2019~" as g where DATE(lpep_pickup_datetime) = '2019-09-18' and DATE(lpep_dropoff_datetime) = '2019-09-18';

Query for Ques 4 : select DATE(lpep_pickup_datetime) as day ,sum(trip_distance) as trip_dist from "green_taxi_data_2019~" as g group by DATE(lpep_pickup_datetime) order by sum(trip_distance) desc;



select t."Borough",sum(g.total_amount) as total_fare,t."Zone",t.service_zone,g.lpep_pickup_datetime,g.lpep_dropoff_datetime,g."DOLocationID",g.trip_distance,g.fare_amount,g.tip_amount,g.total_amount from taxi_lookup as t ,"green_taxi_data_2019~" as g where t."LocationID"= g."PULocationID" and DATE(g.lpep_pickup_datetime)='2019-09-18' group by t."Borough" having sum(g.total_amount)>50000;

Query for ques 5 : 
select t."Borough",sum(g.total_amount) as total_fare from taxi_lookup as t ,"green_taxi_data_2019~" as g where t."LocationID"= g."PULocationID" and DATE(g.lpep_pickup_datetime)='2019-09-18' group by t."Borough" having sum(g.total_amount)>50000;


Query for ques 6:
select joined_table."pickup_zone",joined_table.tip_amount,filtered_lookup.dropoff_zone from (select t."Zone"as Pickup_Zone,g.lpep_pickup_datetime,g.lpep_dropoff_datetime,g."DOLocationID",t."LocationID",g.tip_amount from "green_taxi_data_2019~" g, taxi_lookup t where g."PULocationID"=t."LocationID" and t."Zone"='Astoria')joined_table , (select "Zone" as Dropoff_Zone,"LocationID" from taxi_lookup )filtered_lookup where filtered_lookup."LocationID"=joined_table."DOLocationID" order by joined_table.tip_amount desc;