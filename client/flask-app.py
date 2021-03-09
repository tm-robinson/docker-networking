from flask import Flask

import requests
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello():
    servername = os.getenv('SERVER')

    #r = requests.get('http://127.0.0.1:5000/')
    #r = requests.get('http://host.docker.internal:5000/')
    #r = requests.get('http://docker-networking-server:5000/')
    url = 'http://' + servername + ':5000/'
    print("requesting url " + url, flush=True)
    r = requests.get(url)
    responsetext = r.text
    print("got response " + responsetext, flush=True)
    return 'Server returned: ' + responsetext
