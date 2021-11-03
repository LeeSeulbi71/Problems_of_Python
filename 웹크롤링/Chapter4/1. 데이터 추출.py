from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
from requests.models import codes

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '377300'
]

for code in codes:

    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text

    Soup = BeautifulSoup(html, 'html.parser')
    price = Soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)