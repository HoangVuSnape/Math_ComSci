import requests

url = "https://diemthi.tuyensinh247.com/diem-chuan/dai-hoc-fpt-FPT.html?success=true&ad_id=5e6ae67c7f8b9a495c8b4567&countdown_info=[object Object]"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
