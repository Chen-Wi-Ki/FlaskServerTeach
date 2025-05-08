from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# POST Method
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = f"{data.get('name')}"
    password = f"{data.get('password')}"
    return jsonify(message=f'Your name is {name},password is {password}')