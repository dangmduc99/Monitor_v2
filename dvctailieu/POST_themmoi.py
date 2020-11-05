import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvctailieuquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDQ4ODQzMSwiZXhwIjoxNjA0NDkyMDMxfQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.skoYbAV-XQm6o1F8i5sPMr5jR5zu3wyrJdjUJM3RTbRIHdhWeH9fikhhojKagq7NONi_Gw__Dq2cLWFBWgkWPA"

CREATE_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_tailieu():
    url = ROOT_URL + "ThemMoi"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        'MaHoSo': get_random_string(10),
        'LoaiTaiLieu': get_random_string(10),
        'TenTaiLieu': get_random_string(10),
        'CreatedDate': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'CreatedBy': get_random_string(10),
        'ModifiedBy': get_random_string(10)
    }
    
    files=[
        ('TaiLieu', open('/home/ducdm/Pictures/122953568_652145808817518_4137528532679010030_n.png','rb'))
    ]
    response = requests.request("POST", url, headers=headers, data = data, files=files)


    if response.status_code == 200:
        data['statusCode'] = 200
        data['ID'] = json.loads(response.text)["ID"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        CREATE_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(response)
        CREATE_DATA.append(data)


for i in range(100):
    post_tailieu()

with open('POST_themmoi.json', 'w') as f:
    json.dump(CREATE_DATA, f)
