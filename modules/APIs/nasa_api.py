import webbrowser
from requests import get

API_KEY = '2J5KBhpGWy3goE1wQ5ZYDD3dZU0a5GZZkOALpyoD'

def imgtoday():
    api_req = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
    req_json = get(api_req).json()
    req_img = req_json['hdurl']
    webbrowser.open(req_img)
