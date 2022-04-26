from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options= webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)  #"./chromedriver.exe"
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"

browser.get(url)


#왕복 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[1]/button[2]').click()

#출발지 인천 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[5]').click()

#도착지 밴쿠버 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div[2]/button[4]')

#가는날 선택 클릭(캘린더 오픈)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

#로딩창 기다리는법
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '')))
except:
    print("Fail")



