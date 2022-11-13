import json
import datetime
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
machine = pyttsx3.init()
json_open = open("commands.json", encoding='utf-8')
commands = json.load(json_open)
time = datetime.datetime.now()
time_t = time.strftime("%H:%M")
date = datetime.date.today()
date_formatted = '{}/{}/{}'.format(date.day, date.month, date.year)

data_space = commands['nasa']['space image']
data_hours = commands['date and hour']['hours']
data_day = commands['date and hour']['day']
data_temperature = commands['weather']['temperature']
data_wiki = commands['search']['wikipedia']
data_google = commands['search']['google']
data_youtube = commands['search']['youtube']

try:
    with sr.Microphone() as source:
        audio = r.listen(source)
        spc = str(r.recognize_google(audio, language='pt-BR'))
except KeyboardInterrupt:
    print('the program had a problem')
