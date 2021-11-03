import requests
from bs4 import BeautifulSoup


header = {'User-agent':'Mozila/2.0'}
#모질라 웹브라우저로 접속한 것처럼 보여줌
response = requests.get("https://news.naver.com/", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.lnk_hdline_article')

print(title.text.strip())