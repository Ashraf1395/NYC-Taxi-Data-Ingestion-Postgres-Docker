# NYC Taxi Data Ingestion and Analysis

## Overview

This project involves setting up a Dockerized PostgreSQL database for NYC taxi data, creating a data pipeline, performing analysis, and deploying infrastructure using Terraform. The README provides step-by-step instructions and queries for various tasks.

## Docker Setup

### PostgreSQL Container

Run the following Docker command to start a PostgreSQL container:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="ashraf" \
  -e POSTGRES_DB="nyc_taxi" \
  -v c:/Users/DELL/Desktop/projects/NYC-Taxi-Data-Ingestion-Postgres-Docker/postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=postgres-network \
  --name pg-database \
  postgres:13
```

### pgAdmin Container

Launch a pgAdmin container with the following command:

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="ashraf@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="ashraf" \
  -p 8080:80 \
  --network=postgres-network \
  --name=pg-admin \
  dpage/pgadmin4
```

## Data Pipeline

### Building Docker Image

Build a Docker image for the data ingestion pipeline:

```bash
docker build -t taxi_data_ingestion:v001 .
```

### Running Data Pipeline Container

Run the data ingestion pipeline container:

```bash
docker run -it \
  --network=postgres-network \
  --name=ingestion_pipeline \
  taxi_data_ingestion:v002 \
  --user=root \
  --password=ashraf \
  --host=pg-database \
  --db=nyc_taxi \
  --table_name=green_taxi_data
```

## Docker Compose

Docker Compose is used to orchestrate multiple containers. It provides a way to define and run multi-container Docker applications. In this project, it is used to define and run the entire stack in a more organized manner.

To deploy the entire stack using Docker Compose:

```bash
docker-compose up
```

In detached mode:

```bash
docker-compose up -d
```

To stop the containers:

```bash
docker-compose down
```

## Terraform Setup

1. Install Terraform and add it to your system path.
2. Initialize Terraform:

    ```bash
    terraform init
    ```

3. View the planned changes:

    ```bash
    terraform plan
    ```

4. Deploy the architecture:

    ```bash
    terraform apply
    ```

5. To destroy the infrastructure:

    ```bash
    terraform destroy
    ```

### Purpose of Terraform

Terraform is used in this project to deploy infrastructure for practicing GCP Storage and BigQuery datasets. It helps automate the provisioning and management of cloud resources.

## GCP Storage and BigQuery Deployment (Practice)

To practice deploying GCP Storage and BigQuery datasets, refer to the relevant Terraform configurations and scripts in the `terraform/` directory.

## Analysis Queries

### Question 3: Count of Taxi Trips on September 18, 2019

This query retrieves the count of taxi trips that both started and finished on September 18, 2019.

```sql
SELECT COUNT(*)
FROM "green_taxi_data_2019~" AS g
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' AND DATE(lpep_dropoff_datetime) = '2019-09-18';
```

### Question 4: Daily Total Trip Distance on September 18, 2019

This query calculates the total trip distance for each day in descending order, focusing on September 18, 2019.

```sql
SELECT DATE(lpep_pickup_datetime) AS day, SUM(trip_distance) AS trip_dist
FROM "green_taxi_data_2019~" AS g
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY sum(trip_distance) DESC;
```

### Question 5: Total Fare Amount by Borough on September 18, 2019

This query provides the total fare amount for each borough where the total amount exceeds $50,000, focusing on pickups on September 18, 2019.

```sql
SELECT t."Borough", SUM(g.total_amount) AS total_fare
FROM taxi_lookup AS t, "green_taxi_data_2019~" AS g
WHERE t."LocationID" = g."PULocationID" AND DATE(g.lpep_pickup_datetime)='2019-09-18'
GROUP BY t."Borough"
HAVING SUM(g.total_amount) > 50000;
```

### Question 6: Tip Amounts for Trips Originating in Astoria on September 18, 2019

This query retrieves the tip amounts for trips that originated in Astoria on September 18, 2019, along with the corresponding drop-off zones.

```sql
SELECT joined_table."pickup_zone", joined_table.tip_amount, filtered_lookup.dropoff_zone
FROM (
  SELECT t."Zone" AS Pickup_Zone, g.lpep_pickup_datetime, g.lpep_dropoff_datetime, g."DOLocationID", t."LocationID", g.tip_amount
  FROM "green_taxi_data_2019~" g, taxi_lookup t
  WHERE g."PULocationID" = t."LocationID" AND t."Zone" = 'Astoria'
) joined_table,
(
  SELECT "Zone" AS Dropoff_Zone, "LocationID"
  FROM taxi_lookup
) filtered_lookup
WHERE filtered_lookup."LocationID" = joined_table."DOLocationID"
ORDER BY joined_table.tip_amount DESC;
```

These queries are designed to address specific analytical questions related to taxi trip data, providing insights into trip counts, daily trip distance, fare amounts by borough, and tip amounts for trips originating in Astoria.
