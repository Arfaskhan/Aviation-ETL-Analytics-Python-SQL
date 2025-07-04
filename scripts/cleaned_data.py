import pandas as pd
import pymysql

db_config = {
    'host':'localhost',
    'user':'root',
    'password': 'root',
    'database':'aviation_db'
}

connections = pymysql.connect(**db_config)
cursor = connections.cursor()

data = pd.read_sql('select * from flight_data',connections)
data_is_null = data.columns[data.isnull().any()]
data_list = data_is_null.to_list()
for a in range(len(data_list)):
    if type(data[data_list[a]]) == int:
        data[data_list[a]] = data[data_list[a]].fillna(1).astype(int)
    else:
        data[data_list[a]] = data[data_list[a]].fillna('unknown')
