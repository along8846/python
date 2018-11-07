import json
from flask import make_response
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/home', methods=['GET'])
def index():
    return 'hello world!'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return 'please register!'
    elif request.method == 'POST':
        user = request.form['username']
        return 'hello', user

if __name__ == '__main__':
    app.run(debug=True)


