import requests

url = 'http://127.0.0.1:5000/submit'
payload = {'name': 'wiki',
           'password': '123456'}        

response = requests.post(url, json=payload)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())