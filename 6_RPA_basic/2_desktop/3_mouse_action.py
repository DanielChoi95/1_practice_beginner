import pyautogui

# pyautogui.sleep(3) #3초 대기
# print(pyautogui.position())

#pyautogui.click(67, 26, duration=1) #1초동안 좌표로 이동후 클릭

#pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
#pyautogui.click(clicks=500) #초고속으로 클릭함

pyautogui.moveTo(200,200)
pyautogui.mouseDown() #마우스 누른 상태
pyautogui.moveTo(300,300)
pyautogui.mouseUp() #마우스 떼기

pyautogui.moveTo()
pyautogui.drag(100, 0, duration=0.25) #현재 위치 기준으로 드래그 / 너무 빠른동작으로 드래그 수행이 안되면 duration 줘야함
pyautogui.dragTo()

pyautogui.scroll(300) #양수이면 위, 음수이면 아래로 스크롤