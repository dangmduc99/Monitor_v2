import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcchungchidgdquandinh/"
AUTHORIZATION = ""

GET_DATA = []

with open('POST_themmoi.json') as f:
  createData = json.load(f)

def get_tailieu(Id):
    url = ROOT_URL + "LayTheoSoChungChi?SoChungChi=" + Id
    data = {}
    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = data)


    if (response.status_code == 200 and len(response.text) > 2):
        data = json.loads(response.text)[0]
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        GET_DATA.append(data)

    else:
        if (len(response.text) == 2):
            data['statusCode'] = 404
            data['error'] = 'Not Found'
            data['time'] = response.elapsed.total_seconds()
            data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(data)
            GET_DATA.append(data)
        else:
            data['statusCode'] = response.status_code
            data['error'] = json.loads(response.text)["error"]
            data['time'] = response.elapsed.total_seconds()
            data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(data)            
            GET_DATA.append(data)

for ob in createData:
    if ("SoChungChi" in ob):
        get_tailieu(ob['SoChungChi'])
    else:
        continue

with open('GET_laytheosochungchi.json', 'w') as f:
    json.dump(GET_DATA, f)



