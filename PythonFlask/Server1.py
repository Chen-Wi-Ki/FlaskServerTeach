from flask import Flask, request, jsonify
from datetime import datetime
import math
import pandas as pd

app = Flask(__name__)

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
    bmi = round(weight / height **2,2)# bmi count
    today = datetime.today()# age count
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    df = pd.read_csv('BMI_Normal.csv')
    matched_rows = df[df['age'] == age].iloc[0]
    print(matched_rows)
    bmi_judge = 'wrong data'
    if gender=='male':
        if bmi<matched_rows['male_min']:
            bmi_judge='Too thin'
        elif bmi>=matched_rows['male_min'] and bmi<=matched_rows['male_max']:
            bmi_judge='Normal'
        else:
            bmi_judge='Too fat'
    elif gender=='female':
        if bmi<matched_rows['female_min']:
            bmi_judge='Too thin'
        elif bmi>=matched_rows['female_min'] and bmi<=matched_rows['female_max']:
            bmi_judge='Normal'
        else:
            bmi_judge='Too fat'
        
    return jsonify(message=f'Your AGE={age},BMI={bmi},{bmi_judge}.')