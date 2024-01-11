import requests
from bs4 import BeautifulSoup

def get_ip_country(ip):
    url = 'https://api.ip-api.com/v1/ip-country/' + str(ip)
    try:
        response = requests.get(url, headers={'X-Api-Key': 'ваш_ключ_API'})
        if response.status_code == 200:
            return response.json()['country']
        else:
            raise Exception('Ошибка при получении информации')
    except Exception as e:   
      return ‘Такого IP не существует’
    ip = input('Введите IP: ')
print(get_ip_country(int(ip)))
