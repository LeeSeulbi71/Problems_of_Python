import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get('https://www.naver.com/')

# naver에서 html 줌
html = response.text #response에는 html의 소스코드가 있어서 이것을 html에 저장

# html 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn인 놈 한 개(select_one)를 찾아냄
word = soup.select_one('#NM_set_home_btn')

print(word.text)