import requests
import sys

servername = sys.argv[1]

#r = requests.get('http://127.0.0.1:5000/')
#r = requests.get('http://host.docker.internal:5000/')
#r = requests.get('http://docker-networking-server:5000/')
r = requests.get('http://' + servername + ':5000/')
print(r.text)
