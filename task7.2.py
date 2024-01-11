from bs4 import  BeautifulSoup
import requests 
import datetime

def getWeather(city):
    URL = "https://yandex.ru"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.3"
    }

    def get_html(url, params=None):
        r = requests.get(f"{URL}{url}", headers=HEADERS, params=params)
        return r.text

    def parse_date(soup):
        temperatures = soup.find_all("span", class_="weather__temperature")
        
        for temperature in temperatures:
            if "℉" in temperature.
