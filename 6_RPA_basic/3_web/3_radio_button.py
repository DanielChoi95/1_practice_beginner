from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio') #구글에 w3school radiobutton

browser.switch_to.frame('iframeResult') #frame 전환 / 이걸 안넣어주면 xpath에 접근 못함

elem = browser.find_element_by_xpath('//*[@id="html"]')

#선택이 안 되어 있으면 선택하기
if elem.is_selected() == False:
    elem.click()
else:
    pass

time.sleep(5)




