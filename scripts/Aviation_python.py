import re
import requests
import pymysql

api_key = 'd4d06f5ad90c3947b592b9efe2785acf'

url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&arr_iata=DXB"

data_req = requests.get(url)

data = data_req.json()

db_config = {
    'host':'localhost',
    'user':'root',
    'password': 'root',
    'database':'aviation_db'
}
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

for i in range(len(data['data'])):
    Flight_data = {
       'airline_name': data['data'][i]['airline']['name'],
        'departure_airport' : data['data'][i]['departure']['airport'],
        'terminal': data['data'][i]['departure']['terminal'] if re.match(r'^\d+$', str(data['data'][i]['departure']['terminal'])) else 1,
        'departure_time' : data['data'][i]['departure']['scheduled'],
        'flight_date' : data['data'][i]['flight_date'],
        'flight_status': data['data'][i]['flight_status'],
        'arrival_airport': data['data'][i]['arrival']['airport'],
        'arrival_terminal' : data['data'][i]['arrival']['terminal'],
        'arrival_time': data['data'][i]['arrival']['scheduled'],
    }
    try :
        insert_query = """
            insert into flight_data(airline_name,departure_airport,terminal,departure_time,flight_date,flight_status,arrival_airport,arrival_terminal,arrival_time)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """

        cursor.execute(insert_query,(
            Flight_data['airline_name'],
            Flight_data['departure_airport'],
            Flight_data['terminal'],
            Flight_data['departure_time'],
            Flight_data['flight_date'],
            Flight_data['flight_status'],
            Flight_data['arrival_airport'],
            Flight_data['arrival_terminal'],
            Flight_data['arrival_time']


        ))
        connection.commit()
    except Exception as e:
        print(f'Data_line : {i+1} , Error:{e}')
cursor.close()
connection.close()


