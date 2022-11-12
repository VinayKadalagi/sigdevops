from flask import Flask
import json
import os
app = Flask(__name__)

def read_Json_Doc():
    script_dir = os.path.dirname(__file__) 
    json_file = open(os.path.join(script_dir, 'data.json'))
    data = json.load(json_file)
    return data

@app.route('/')
def hello_world():
    return read_Json_Doc()