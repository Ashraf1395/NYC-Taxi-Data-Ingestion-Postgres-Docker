import pandas as pd
from sqlalchemy import create_engine
from time import time
print(pd.__version__)

#Connecting to postgres database
engine=create_engine('postgresql://root:ashraf@localhost:5432/nyc_taxi')

df= pd.read_csv(r'C:\Users\DELL\Desktop\projects\NYC-Taxi-Data-Ingestion-Postgres-Docker\green_tripdata_2021-01.csv')
df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)

print(df.head())  
#Creating schema statement
print(pd.io.sql.get_schema(df,name='green_taxi_data',con=engine))

print('Starting chunkwise insertion into postgres db nyc_taxi ')
#Doing it Chunk wise
df_iter= pd.read_csv(r'C:\Users\DELL\Desktop\projects\NYC-Taxi-Data-Ingestion-Postgres-Docker\green_tripdata_2021-01.csv',iterator=True,chunksize=20000)

try:        
    i=0
    while True:        
        t_start= time()
        df_chunk=next(df_iter)
        i+=1  
        #Converting into datetime format
        df_chunk.lpep_pickup_datetime=pd.to_datetime(df_chunk.lpep_pickup_datetime)
        df_chunk.lpep_dropoff_datetime=pd.to_datetime(df_chunk.lpep_dropoff_datetime)
        
        #Ingesting data into postgres 
        df_chunk.to_sql(name='green_taxi_data',con=engine,if_exists='append')
        t_end=time()
        print(f'Inserted Chunk number {i}, took {t_end - t_start}')
        print(f'Shape and Size {df_chunk.shape}')
except StopIteration:
    print('All Chunks of data ingested into postgres db.')