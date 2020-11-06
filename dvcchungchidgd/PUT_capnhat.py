import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcchungchidgdquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDU5MzE4OCwiZXhwIjoxNjA0NTk2Nzg4fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.9LEmRHvt8K9M8gbAAz1k9o5VtlUGI0TTzRHKgcu18xqCX_cUgXli8kmifhC_FvBNARLvv8ef1Jb36QzeXt3wIA"

UPDATE_DATA = []

with open('POST_themmoi.json') as f:
    createData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_chungchi(id):
    url = ROOT_URL + "CapNhat"

    data = {
        'ID': id,
        'NgayCoHieuLuc': get_random_string(10),
        'NgayHetHieuLuc': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'ModifiedBy': get_random_string(10)
    }


    files=[
        ('ChungChi', open('C:/Users/dangm/Desktop/Monitor_v2/dvcchungchidgd/POST_user.json','rb'))
    ]

    headers = {
        'Authorization': AUTHORIZATION,
    }

    response = requests.request("PUT", url, headers=headers, data = data, files = files)


    if response.status_code == 200:
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        UPDATE_DATA.append(data)

    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        UPDATE_DATA.append(data)

for ob in createData:
    if ("ID" in ob):
        put_chungchi(ob['ID'])

with open('PUT_capnhat.json', 'w') as f:
    json.dump(UPDATE_DATA, f)