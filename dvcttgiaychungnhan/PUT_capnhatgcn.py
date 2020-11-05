import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcttgiaychungnhanquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDQ4NjgwOCwiZXhwIjoxNjA0NDkwNDA4fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.Zf8PahOykU5s9nntypIIekHYEgQbQ2rg0d_XhgWcZSRGhLSDYhV-Gjy88aHWCG-fTqWofU4VdvJwX4-4r9mARQ"

PUT_DATA = []

with open('POST_themmoi.json') as f:
  createData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_gcn(id):
    url = ROOT_URL + "CapNhatGCN"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        'SoSeri': get_random_string(10),
        'SoVaoSoCapGCN': get_random_string(10),
        'DiaChiThuaDat': get_random_string(10),
        'DienTich': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'ModifiedBy': get_random_string(10)
    }

    data['ID'] = id
    
    files=[
        ('GiayChungNhan', open('/home/ducdm/Pictures/122953568_652145808817518_4137528532679010030_n.png','rb'))
    ]
    response = requests.request("PUT", url, headers=headers, data = data, files=files)


    if response.status_code == 200:
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        PUT_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(response)
        PUT_DATA.append(data)


for ob in createData:
    if("ID" in ob):
        put_gcn(ob['ID'])
    else:
        continue


with open('PUT_capnhatgcn.json', 'w') as f:
    json.dump(PUT_DATA, f)
