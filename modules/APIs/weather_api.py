from requests import get
import modules.main as main

API_KEY = 'cb3d4b7abf1326d2ba1520686ee7c8c8'

def temperature():
    search_temp = main.spc.replace('Maria qual é a temperatura em', '')
    city = search_temp
    api_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    json_req = get(api_link).json()
    temp_city = json_req['main']['temp'] - 273.15
    temp_formatted = f'{temp_city:.0f} Graus'
    main.machine.say(temp_formatted)
    main.machine.runAndWait()
