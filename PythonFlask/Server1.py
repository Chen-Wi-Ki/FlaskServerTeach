from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# GET Method
@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'World') #'World' is default
    password = request.args.get('password', 'None') #‘None' is default
    if password=='None':
        return f'Hello {name}...'
    else:
        if name=='wiki' and password=='123456':
            return f'Hello {name}, welcome to system.'
        elif name=='chen' and password=='456789':
            return f'Hello {name}, welcome to system.'
        else:
            return f'password error!!!'