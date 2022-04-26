from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp') #구글에 w3school radiobutton

browser.switch_to.frame('iframeResult') #frame 전환 / 이걸 안넣어주면 xpath에 접근 못함

elem = browser.find_element_by_xpath('//*[@id="male"]') #성공

elem.click()

browser.switch_to.default_content() #상위로 빠져나옴

elem = browser.find_element_by_xpath('//*[@id="male"]') #실패
