from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/html/')

time.sleep(3)

#특정 영역 스크롤
elem= browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

#1. ActionChains
actions= ActionChains(browser)
actions.move_to_element(elem).perform()

#2. 좌표 정보 이용
xy= elem.location_once_scrolled_into_view #함수가 아니라 변수임 dict형태

