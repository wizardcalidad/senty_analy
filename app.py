from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Semicolon Devs'

@app.route('/ping')
def ping():
    return 'pong!'
