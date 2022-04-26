from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()

browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
#browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()


first_name= browser.find_element_by_xpath('//*[@id="fname"]')
first_name.send_keys("나도")

last_name= browser.find_element_by_xpath('//*[@id="lname"]')
last_name.send_keys("코딩")

country= browser.find_element_by_xpath('//*[@id="country"]/option[2]')
country.click()

subject= browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subject.send_keys("퀴즈 완료했습니다.")

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
time.sleep(5)
browser.quit()