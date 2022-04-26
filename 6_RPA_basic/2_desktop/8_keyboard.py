import pyautogui

w= pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

pyautogui.write("12345")
pyautogui.write("CDHcoding", interval=0.25)
#영문이랑 숫자만 가능

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
#t e s t 순서대로 적고 왼쪽방향키 2번, 오른쪽 방향키 1번, l a 순서대로 적고 엔터 입력
#구글에 automate the boring stuff with python 검색 / ctrl+f keyboard attr검색

#특수 문자
pyautogui.keyDown("Shift")
pyautogui.press("4")
pyautogui.keyUp("Shift")

#조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

#간편한 조합키
pyautogui.hotkey("ctrl", "a") #순서대로 누르고 역순으로 뗌

import pyperclip
pyperclip.copy("나도코딩") #나도코딩 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") #붙여넣기

#ctrl + alt + del 누르면 FAILSAFE