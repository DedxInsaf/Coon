import requests
import json
#Задание 1
info = input()
response = requests.get(
    f"http://ip-api.com/json/{info}"
)

json_data = json.loads(response.text)

if json_data['status'] != 'success':
    print("Такого IP не существует")
else:
    print(json_data['country'])

#Задание 2
def get_weather(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    temp = bs.find('span', 'tempvalue tempvalue_with-unit')

    if temp is not None:
        print(f"Погода на сегодня: {temp.text}°C")

        week = bs.find('div', 'forecast-briefly__days')
        days = week.findAll('div', 'forecast-briefly__day')

        print('Погода на неделю:')
        for day in days:
            day_name = day.find('div', 'forecast-briefly__name')
            day_temp = day.find('div', 'forecast-briefly__temp-day')
            print(f'{day_name}: {day_temp}°C')
        else:
            print("Не удалось получить прогноз")
            return
