#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
from sqlalchemy import create_engine
from time import time


# In[11]:


# pd.read_csv('green_tripdata_2019-09.csv.gz', compression='gzip')


# In[57]:


dtypes = {
    'VendorID': 'Int64', 
    'lpep_pickup_datetime': 'object', 
    'lpep_dropoff_datetime': 'object',
    'store_and_fwd_flag': 'object',
    'RatecodeID': 'float64',
    'PULocationID': 'int64',
    'DOLocationID': 'int64',
    'passenger_count': 'Int64',
    'trip_distance': 'float64',
    'fare_amount': 'float64',
    'extra': 'float64',
    'mta_tax': 'float64',
    'tip_amount': 'float64',
    'tolls_amount': 'float64',
    'ehail_fee': 'float64',
    'improvement_surcharge': 'float64',
    'total_amount': 'float64',
    'payment_type': 'Int64',
    'trip_type': 'Int64',
    'congestion_surcharge': 'float64',
    'tolls_amount': 'float64',
}


# In[58]:


df = pd.read_csv('green_tripdata_2019-09.csv.gz', compression='gzip', dtype=dtypes, parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'])
# df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
# df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
df


# In[30]:


# database engine for connections
engine = create_engine('postgresql://root:root@localhost:5432/taxi_db')


# In[31]:


engine.connect()


# In[32]:


print(pd.io.sql.get_schema(df, name='green_trips_data', con=engine))


# In[59]:


# read in chunks of rows with an iterator
df_iter = pd.read_csv(
    'green_tripdata_2019-09.csv.gz', 
    compression='gzip', 
    dtype=dtypes, 
    parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'], 
    iterator=True, 
    chunksize=75000
)
df = next(df_iter)


# In[36]:


# redo the timestamp convertion
# df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
# df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


# In[ ]:


# df.to_sql(name='green_trips_data', con=engine, if_exists='replace')


# In[60]:


df.head(n=0).to_sql(name='green_trips_data', con=engine, if_exists='replace')


# In[61]:


while True:
    t_start = time()
    
    df = next(df_iter)
    df.to_sql(name='green_trips_data', con=engine, if_exists='append')

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    t_end = time()

    print(f'Inserted a chunk of data... {len(df)} rows %.3f' % (t_end - t_start))


# In[44]:


df.info()

