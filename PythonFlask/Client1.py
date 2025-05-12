import requests
url = 'http://wiciar.com/bmi/submit'
payload = {'name': 'wiki',
           'password': 'abc123',
           'birthday':'1990-04-24',
           'gender':'male',
           'height':1.88,
           'weight':44}
response = requests.post(url, json=payload)
print('Status Code:', response.status_code)
print('Response JSON:', response.json())