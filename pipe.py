import pandas as pd

print(pd.__version__)

df= pd.read_csv(r'C:\Users\DELL\Desktop\projects\NYC-Taxi-Data-Ingestion-Postgres-Docker\green_tripdata_2021-01.csv')

print(df.head())

print(pd.io.sql.get_schema(df,name='green_taxi_data'))