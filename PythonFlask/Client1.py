import requests

url = 'http://127.0.0.1:5000/submit'
payload = {'name': 'wiki',
           'password': '123456',
           'birthday':'1990-04-24',
           'gender':'male',
           'height':1.75,
           'weight':110}

response = requests.post(url, json=payload)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())