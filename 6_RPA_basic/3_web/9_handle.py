from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle= browser.current_window_handle
print(curr_handle)

#try it yourself
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles= browser.window_handles #모든 핸들 정보
for handle in handles:
    print(handle) #각 핸들 정보
    browser.switch_to.window(handle) #각 핸들로 이동해서
    print(browser.title) #출력해보면 현재 핸들(브라우저)의 제목 표시

#새로 이동한 브라우저(try it yourself)에서 작업 수행후 종료할때
browser.close()

#이전 핸들로 돌아오기
browser.switch_to.window(curr_handle)
