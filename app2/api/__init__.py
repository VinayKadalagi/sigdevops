from flask import Flask
import requests
import sys

app = Flask(__name__)

def reverse():
    print ("hitting URL app1-service:5000", file=sys.stdout)
    x = requests.get('http://app1-service:5000')
    print (x, file=sys.stdout)
    str = x.json()['message']
    revstr = ""
    for i in str:
        revstr = i + revstr
    return revstr

@app.route('/')
def hello_world():
    reverseword = reverse()
    return { "id": "1", "message": reverseword }
