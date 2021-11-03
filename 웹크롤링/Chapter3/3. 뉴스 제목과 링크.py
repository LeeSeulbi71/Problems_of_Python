import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B9%B4%EC%B9%B4%EC%98%A4')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') #결과는 리스트로

for link in links:
    title = link.text # 태그 안에 텍스트 요소를 가져옴
    url = link.attrs['href'] # href의 속성값을 가져온다
    print(title, url)
