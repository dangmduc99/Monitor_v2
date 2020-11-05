import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcquatrinhxulyhsquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwNDg3NywiZXhwIjoxNjA0NTA4NDc3fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.vto1k5Rjv8Xus1IWcKane4-Zg3ao4Fu9nFC8y9UUApwyRHddIzx-SwyC6UN1qru0Q3DdQc4AwVGh5rKOFW-lHQ"
ROLE = ['CHUYENVIEN', 'LANHDAO']
USER_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_user():
    url = ROOT_URL + "user"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        "username": get_random_string(10),
        "password": get_random_string(10),
        "role": random.choice(ROLE)
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(data))


    if response.status_code == 200:
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        USER_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(response)
        USER_DATA.append(data)


for i in range(100):
    post_user()

with open('POST_user.json', 'w') as f:
    json.dump(USER_DATA, f)
