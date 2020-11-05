import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvchosoquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDM5ODQ1OSwiZXhwIjoxNjA0NDAyMDU5fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.cTa_p0cjtjeTQ9PXntLwXCXIL7Pgk-8F7F_8gEy5xxGSw9v3_onSL8MYuoN98EetZ_aK1SNHmeTgHufAG7cIcQ"

UPDATE_DATA = []

with open('GET_laytheoid.json') as f:
    getData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_profile(id):
    url = ROOT_URL + "CapNhatFull"

    data = {
        "HS_TechID": get_random_string(10),
        "HS_ThuTucHanhChinhTen": get_random_string(10),
        "HS_HoSoId": get_random_string(10),
        "HS_MucDoDVC": get_random_string(10),
        "HS_MaHoSo": get_random_string(10),
        "HS_NgayTiepNhan": get_random_string(10),
        "CBTN_Id": get_random_string(10),
        "HS_TrangThaiCDId": get_random_string(10),
        "HS_NgayHenTra": get_random_string(10),
        "HS_LinhVucMa": get_random_string(10),
        "HS_CachTiepNhan": get_random_string(10),
        "CBTN_Ten": get_random_string(10),
        "HS_ThuTucHanhChinhId": get_random_string(10),
        "TC_Email": get_random_string(10),
        "CQTN_DanhSach": get_random_string(10),
        "HS_ModifiedDate": get_random_string(10),
        "HS_NgayNop": get_random_string(10),
        "HS_LinhVucId": get_random_string(10),
        "HS_LinhVucOrder": get_random_string(10),
        "HS_NgayKetThucXuLy": get_random_string(10),
        "CachThucTra": get_random_string(10),
        "HS_TrangThaiCDTen": get_random_string(10),
        "HS_TrangThaiHSId": get_random_string(10),
        "HS_MaSoBienNhan": get_random_string(10),
        "LoaiKetQuaGiaiQuyet": get_random_string(10),
        "HS_CreateBy": get_random_string(10),
        "HS_SoDen": get_random_string(10),
        "HS_NgayTiepNhanLanDau": get_random_string(10),
        "HS_MaAnhXa": get_random_string(10),
        "TC_DiaChi": get_random_string(10),
        "HS_CreateDate": get_random_string(10),
        "HS_ModifiedBy": get_random_string(10),
        "TC_TenToChuc": get_random_string(10),
        "KQ_ThongTin": get_random_string(10),
        "HS_NgayKyKQ": get_random_string(10),
        "HS_NoiDungCapPhep": get_random_string(10),
        "HS_ThanhPhanKhac": get_random_string(10),
        "HS_ThanhPhanHSQD": get_random_string(10),
        "TC_SoDienThoai": get_random_string(10),
        "HS_DaXoa": get_random_string(10),
        "WFL_TaskList": get_random_string(10),
        "HS_NgayThucTra": get_random_string(10),
        "HS_TrangThaiHSTen": get_random_string(10),
        "HS_LinhVucTen": get_random_string(10)
    }

    data['ID'] = id

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

with open('PUT_capnhatfull.json', 'w') as f:
    json.dump(UPDATE_DATA, f)