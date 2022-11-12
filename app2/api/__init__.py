from flask import Flask
import requests

app = Flask(__name__)


def reverse():
    x = requests.get('http://app1-service:5000')
    str = x.json()['message']
    revstr = ""
    for i in str:
        revstr = i + revstr
    return revstr


@app.route('/')
def hello_world():
    reverseword = reverse()
    return {"id": "1", "message": reverseword}
