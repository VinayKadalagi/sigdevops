from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return { "id": "1", "message": "Hello world" }

