from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# POST Method
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    birthday = datetime.strptime((f"{data.get('birthday')}"), "%Y-%m-%d")
    gender = data.get('gender')
    height = data.get('height')
    weight = data.get('weight')
    
    # bmi count
    bmi = round(weight / height **2,2)
    
    # age count
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    return jsonify(message=f'Your AGE={age},BMI={bmi}')