#프로그램을 실행하면 검색어를 입력 받게 함

import requests
from bs4 import BeautifulSoup

want_search = input("검색하고 싶은 단어: ")


header = {'User-agent':'Mozila/2.0'}
#모질라 웹브라우저로 접속한 것처럼 보여줌
response = requests.get("https://news.naver.com/", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.lnk_hdline_article')