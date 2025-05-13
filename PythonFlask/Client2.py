import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://wiciar.com/bmi/data_get'
payload = {'name': 'wiki2',
           'password': 'abc123'}
print('Json Code:', payload)
response = requests.post(url, json=payload)
print('Status Code:', response.status_code)
#print('Response JSON:', response.json()['message'])
data_list = response.json()['message']
df = pd.DataFrame(data_list)
df['build_time'] = pd.to_datetime(df['build_time'])
df = df.dropna(subset=['bmi', 'build_time'])
df = df.sort_values(by='build_time')
plt.figure(figsize=(10, 5))
plt.plot(df['build_time'], df['bmi'], marker='o', linestyle='-', color='blue', label='BMI')
plt.title('BMI Trend Over Time')
plt.xlabel('Build Time')
plt.ylabel('BMI')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()