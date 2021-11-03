from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
from requests.models import codes
import openpyxl

fpath = r'C:\Users\yongs\GDSC\StudyPython\웹크롤링\Chapter4\data.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active #현재 활성화된 시트 선택

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '377300'
]

row = 2
for code in codes:

    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text

    Soup = BeautifulSoup(html, 'html.parser')
    price = Soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)
    ws[f'B{row}'] = int(price)
    row += 1

wb.save(fpath)