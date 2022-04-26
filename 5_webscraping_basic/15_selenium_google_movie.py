import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximaize_window()

url = "https://play.google.com/store/movies/category/MOVIE"
browser.get(url)

#지정한 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)") #화면 해상도의 높이인 1080위치로 스크롤 내리기

#화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#2초에한번씩 스크롤 내리기
interval = 2

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
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height