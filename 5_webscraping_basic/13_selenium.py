from selenium import webdriver

options= webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)  #"./chromedriver.exe"

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("my id")
browser.find_element_by_id("pw").send_keys("my pw")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

#5. id를 새로 입력

# browser.back()
# browser.forward()
# browser.refresh()