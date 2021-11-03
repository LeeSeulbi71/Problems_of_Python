import requests
from bs4 import BeautifulSoup
import pyautogui

#검색어에 해당하는 query를 바꿔주면 됨!

keyword = pyautogui.prompt("검색어를 입력하세요: ")
response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}') #f-string
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') #결과는 리스트로

for link in links:
    title = link.text # 태그 안에 텍스트 요소를 가져옴
    url = link.attrs['href'] # href의 속성값을 가져온다
    print(title, url)


# pyautogui
# 마우스, 키보드 매크로 라이브러리
# 간단한 입력창 띄우기