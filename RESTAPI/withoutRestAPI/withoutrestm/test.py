from tkinter import END
import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


def get_resource(id):
    r = requests.get(BASE_URL+ENDPOINT+id)
    print(r.status_code)
    print(r.json())


def get_all():
    r = requests.get(BASE_URL+ENDPOINT)
    print(r.status_code)
    print(r.json())


def post_resource():
    stu_data = {
        'rollno': 5,
        'name': 'mallika',
        'age': 10,
    }
    resp = requests.post(BASE_URL+ENDPOINT, data=json.dumps(stu_data))
    print(resp.status_code)
    print(resp.json())


post_resource()
# get_all()
