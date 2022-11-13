import webbrowser
import wikipedia
import modules.main as main
from modules.APIs.weather_api import temperature
from modules.APIs.nasa_api import imgtoday

def controller():
        # hours command
    if main.spc == main.data_hours:
        main.machine.say(main.time_t)
        main.machine.runAndWait()

        #date command
    elif main.spc == main.data_day:
        main.machine.say(main.date_formatted)
        main.machine.runAndWait()

        # temperature command
    elif main.data_temperature in main.spc:
        temperature()

        # search youtube command
    elif main.data_youtube in main.spc:
        search_youtube = main.spc.replace('Maria Pesquise por', '')
        link = f'https://www.youtube.com/results?search_query={search_youtube}'
        webbrowser.open(link)

        # search google command
    elif main.data_google in main.spc:
        search_google = main.spc.replace('Maria busque por', '')
        link = f'https://www.google.com/search?q={search_google}'
        webbrowser.open(link)

        # search wikipedia command
    elif main.data_wiki in main.spc:
        search = main.spc.replace('Maria procure por', '')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(search, 2)
        link = "wikipedia.org/wiki/"
        opensearch = link + search
        webbrowser.open(opensearch)
        main.machine.say(result)
        main.machine.runAndWait()

        # space image command
    elif main.spc == main.data_space:
        imgtoday()
controller()
