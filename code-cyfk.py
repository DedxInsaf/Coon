import requests

# Часть 1: Получение страны по IP
def get_country_by_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data["status"] == "success":
            return data["country"]
        else:
            return "Такого IP не существует"
    else:
        return "Ошибка при выполнении запроса"
info = input()
response = requests.get(
    f"http://ip-api.com/json/{info}"
)

json_data = json.loads(response.text)

if json_data['status'] != 'success':
    print("Такого IP не существует")
else:
    print(json_data['country'])

# Часть 2: Получение погоды
#def get_weather():
    #url = "https://yandex.ru/pogoda"
    #response = requests.get(url)
    
    #if response.status_code == 200:
        # Обработка HTML-страницы и извлечение нужных данных
        # (используйте библиотеки для парсинга HTML, например, BeautifulSoup)
        # В данном примере я просто возвращаю заглушку
       # return "Погода на сегодня: солнечно\nПогода на неделю: переменная облачность"
    #else:
       # return "Ошибка при выполнении запроса"

# Пример использования
#ip = "8.8.8.8"
#country = get_country_by_ip(ip)
#print(f"Страна, соответствующая IP {ip}: {country}")

#weather = get_weather()
#print(f"\nПогода:\n{weather}")