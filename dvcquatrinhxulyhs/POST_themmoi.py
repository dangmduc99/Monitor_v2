import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcquatrinhxulyhsquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwNDg3NywiZXhwIjoxNjA0NTA4NDc3fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.vto1k5Rjv8Xus1IWcKane4-Zg3ao4Fu9nFC8y9UUApwyRHddIzx-SwyC6UN1qru0Q3DdQc4AwVGh5rKOFW-lHQ"

CREATE_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_hs():
    url = ROOT_URL + "ThemMoi"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        "TaskId": get_random_string(10),
        "CreatedBy": get_random_string(10),
        "TaskName": get_random_string(10),
        "NguoiXuLy": get_random_string(10),
        "NoiDungXuLy": get_random_string(10),
        "TrangThai": get_random_string(10),
        "CreatedDate": get_random_string(10),
        "MaHoSo": get_random_string(10),
        "ModifiedDate": get_random_string(10),
        "ModifiedBy": get_random_string(10),
        "NgayXuLy": get_random_string(10)
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(data))


    if response.status_code == 200:
        data['statusCode'] = 200
        data['profileId'] = json.loads(response.text)["ID"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        CREATE_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        CREATE_DATA.append(data)


for i in range(100):
    post_hs()

with open('POST_themmoi.json', 'w') as f:
    json.dump(CREATE_DATA, f)
