import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcttgiaychungnhanquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDQ4NjgwOCwiZXhwIjoxNjA0NDkwNDA4fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.Zf8PahOykU5s9nntypIIekHYEgQbQ2rg0d_XhgWcZSRGhLSDYhV-Gjy88aHWCG-fTqWofU4VdvJwX4-4r9mARQ"

CREATE_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_gcn():
    url = ROOT_URL + "ThemMoi"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        'MaHoSo': get_random_string(10),
        'SoSeri': get_random_string(10),
        'SoVaoSoCapGCN': get_random_string(10),
        'SoThua': get_random_string(10),
        'SoToBanDo': get_random_string(10),
        'DiaChiThuaDat': get_random_string(10),
        'DienTich': get_random_string(10),
        'MaTinh': get_random_string(10),
        'TenTinh': get_random_string(10),
        'MaHuyen': get_random_string(10),
        'TenHuyen': get_random_string(10),
        'MaXa': get_random_string(10),
        'TenXa': get_random_string(10),
        'CreatedDate': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'CreatedBy': get_random_string(10),
        'ModifiedBy': get_random_string(10)
    }
    
    files=[
        ('GiayChungNhan', open('/home/ducdm/Pictures/122953568_652145808817518_4137528532679010030_n.png','rb'))
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
    post_gcn()

with open('POST_themmoi.json', 'w') as f:
    json.dump(CREATE_DATA, f)
