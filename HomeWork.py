import requests
from bs4 import BeautifulSoup

def currensy_rates():
    usd_rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc&aqs=chrome.1.69i57j0i67i131i433l4j0i67j0i67i131i433l4.2338j0j15&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    full_page = requests.get(usd_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    print(f"Курс доллара равен: " + convert[0].text)

currensy_rates()


import main
from main import currensy_rates
