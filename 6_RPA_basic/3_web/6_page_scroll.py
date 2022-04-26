from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://shopping.naver.com/home/p/index.naver')

#무선마우스 입력
elem= browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')
time.sleep(1)
elem.send_keys(Keys.ENTER)

#스크롤 내리기
# #1. 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)')

# #2. 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

#2초에한번씩 스크롤 내리기
interval = 2

#3. 스크롤 계속 내려서 끝까지 가기

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 다시 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if curr_height == prev_height: #현재 높이와 직전 높이가 같다면
        break #while문 탈출, 스크롤 끝
    
    prev_height = curr_height

#맨 위로 올리기
browser.execute_script('window.scrollTo(0,0)')