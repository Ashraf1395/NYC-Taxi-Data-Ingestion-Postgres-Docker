import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os
print(pd.__version__)


# df= pd.read_csv(r'C:\Users\DELL\Desktop\projects\NYC-Taxi-Data-Ingestion-Postgres-Docker\green_tripdata_2021-01.csv')
# df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
# df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)

# print(df.head())  

# #Creating schema statement
# print(pd.io.sql.get_schema(df,name='green_taxi_data',con=engine))

def main(params):
    user=params.user
    password=params.password
    host=params.host
    db=params.db_name
    table_name=params.table_name
    csv_file='data/green_tripdata_2021-01.csv'
    print(f'Starting chunkwise insertion into postgres database {db} with table_name {table_name} ')
    
    #os.system(f"wget {file_url} -O {csv_file}")

    #Connecting to postgres database
    engine=create_engine(f'postgresql://{user}:{password}@{host}:5432/{db}')

    #Doing it Chunk wise
    df_iter= pd.read_csv(csv_file,iterator=True,chunksize=20000)

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
            df_chunk.to_sql(name=table_name,con=engine,if_exists='append')
            t_end=time()
            print(f'Inserted Chunk number {i}, took {t_end - t_start}')
            print(f'Shape and Size {df_chunk.shape}')
    
    except StopIteration:
        print(f'All Chunks of data ingested into postgres database {db}.')


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument('--user', help="Username for postgres")
    parser.add_argument('--password', help="Password for postgres")
    parser.add_argument('--host', help="host for postgres")
    parser.add_argument('--db_name', help="Database name for postgres")
    parser.add_argument('--table_name', help="Table name for postgres")
    args=parser.parse_args()

    main(args)
