import pyautogui
import pyperclip

#pyautogui.mouseInfo() #마우스 좌표, 컬러 등 정보 프로그램 실행
pyautogui.PAUSE = 1

#1. 그림판 실행
pyautogui.hotkey("winleft", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

w= pyautogui.getWindowsWithTitle("제목 없음")[0]

w.maximize() #최대화

#2. 글자입력
pyautogui.click(401, 93) #텍스트 상자 클릭
pyautogui.click(18,203) #흰 영역 클릭
pyperclip.copy("참 잘했어요") #글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") #붙여넣기


#3. 5초 대기후 종료
pyautogui.sleep(5)
w.close() #윈도우 닫기, 저장할 내용있으면 물어봄
pyautogui.press("right")
pyautogui.press("enter")
