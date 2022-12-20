import requests

places = {
    'San Francisco': 'san%20francisco',
    'Cherepovets': 'cherepovets',
    'Sheremetyevo airoport': 'SVO',
}

# if you want to set russian language, replace value 'en' to 'ru'
lang = 'en'

url = 'https://wttr.in/{value}?nTmq&lang={lang}'

for key, value in places.items():
    response = requests.get(url.format(value=value, lang=lang))
    response.raise_for_status()
    print(response.text.replace(value, key))
