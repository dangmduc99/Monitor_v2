import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcquatrinhxulyhsquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwNDg3NywiZXhwIjoxNjA0NTA4NDc3fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.vto1k5Rjv8Xus1IWcKane4-Zg3ao4Fu9nFC8y9UUApwyRHddIzx-SwyC6UN1qru0Q3DdQc4AwVGh5rKOFW-lHQ"

UPDATE_DATA = []

with open('POST_themmoi.json') as f:
    getData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_profile(id):
    url = ROOT_URL + "CapNhat"

    data = {
        "NguoiXuLy": get_random_string(10),
        "NoiDungXuLy": get_random_string(10),
        "TrangThai": get_random_string(10),
        "ID": id,
        "ModifiedDate": get_random_string(10),
        "ModifiedBy": get_random_string(10),
        "NgayXuLy": get_random_string(10)
    }


    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data = json.dumps(data))


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

for ob in getData:
    if ("ID" in ob):
        put_profile(ob['ID'])

with open('PUT_capnhat.json', 'w') as f:
    json.dump(UPDATE_DATA, f)