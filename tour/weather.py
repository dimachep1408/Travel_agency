from requests import get


api = 'weather api'
dict_icons = {}
for i in ['Tokyo', 'Paris', 'Madrid']:
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={i}&appid={api}'
    answer = get(url)
    if answer.status_code == 200:
        data = answer.json()
        icon = data['list'][0]['weather'][0]['icon'] + '.png'
        dict_icons[i] = icon