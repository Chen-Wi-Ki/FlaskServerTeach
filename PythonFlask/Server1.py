from flask import Flask, request, jsonify
from datetime import datetime
import math
import pandas as pd
import os

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
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    df = pd.read_csv('BMI_Normal.csv')
    matched_rows = df[df['age'] == age].iloc[0]
    #print(matched_rows)
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
    filename = f"UserData\{name}.csv"
    if os.path.exists(filename): # file exists
        load_df = pd.read_csv(filename)# file load
        stored_password = str(load_df.iloc[0]['password'])# password load
        if stored_password != password:# password incorrect
            return jsonify(message="password error!"), 403
        else:# password correct
            user_data = { #Save Data
                'height': height,
                'weight': weight,
                'bmi': bmi,
                'bmi_judge':bmi_judge,
                'build_time':today
            }
            load_df = pd.concat([load_df, pd.DataFrame([user_data])], ignore_index=True)
            load_df.to_csv(filename, index=False)
    else:# no files
        user_data = {#Save Data
            'password': password,
            'birthday': birthday,
            'gender': gender,
            'height': height,
            'weight': weight,
            'bmi': bmi,
            'bmi_judge':bmi_judge,
            'build_time':today
        }
        save_df = pd.DataFrame([user_data])
        save_filename = f"UserData\{name}.csv".replace("/", "_")
        save_df.to_csv(save_filename, index=False)
    return jsonify(message=f'Your AGE={age},BMI={bmi},{bmi_judge}.')