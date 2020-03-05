# importing the requests library 
import requests 
from db import DBmodel

from datetime import datetime

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

URL = {
    "br": "https://api.nestoria.com.br/api",
    "de": "https://api.nestoria.de/api",
    "es": "https://api.nestoria.es/api",
    "fr": "https://api.nestoria.fr/api",
    "in": "https://api.nestoria.in/api",
    "it": "https://api.nestoria.it/api",
    "mx": "https://api.nestoria.mx/api",
    "uk": "https://api.nestoria.co.uk/api",
    }

db = DBmodel()
db_col_names = db.get_column_names('responses_table')
listing_val = []
PARAMS = {  
    "encoding": "json",
    "pretty": 1,
    "action": "search_listings"
  }
def get_input_data():
    cn = input("Enter the counry(e.g 'es') : ")
    tp = input("Enter the listing_type(e.g 'buy') : ")
    pn = input("Enter the place_name(e.g 'valencia') : ")
    PARAMS.update({"country": cn, "listing_type": tp, "place_name": pn})

def call_api(url, params):
    try:
        response = requests.get(url = url, params = params)
        data = response.json() 
        request_data = data['request']
        request_data.update({'insert_time': date_time})
        listings = data["response"]['listings']
        print("Getting data from API is Successfull")
    except e:
        print("Getting data from API is failed.")
        return
    for row in listings:
        tmp = []
        for col in db_col_names:
            try: 
                tmp.append(row[col])
            except:
                if col == 'insert_time':
                    tmp.append(date_time)
                else:
                    tmp.append('')
        listing_val.append(tmp)
    db.insert_request(request_data)
    db.insert_listings(listing_val)
    db.cursor.close()
    db.conn.close()
    
if __name__ == '__main__':
    get_input_data()
    call_api(URL[PARAMS['country']], PARAMS)