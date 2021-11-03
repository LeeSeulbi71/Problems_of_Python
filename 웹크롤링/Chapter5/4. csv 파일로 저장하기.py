from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://naver.com')
browser.implicitly_wait(10) #로딩이 끝날 때, 10초까지는 기다려줌

#쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

#검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

#스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤 -> 반복문
while 1:
    # 맨 아래로 스크롤을 내림
    browser.find_element_by_css_selector("body").send_keys(Keys.END) #body 태그는 모든 사이트에 있음

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)
    
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

#파일 생성
f = open(r'C:\Users\yongs\GDSC\StudyPython\웹크롤링\Chapter5\data.csv', 'w', encoding='CP949', newline = '')

#상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")
csvWriter = csv.writer(f)

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)

    #데이터 쓰기
    csvWriter.writerow([name, price, link]) # 한행을 추가하겠음

#파일 닫기
f.close()