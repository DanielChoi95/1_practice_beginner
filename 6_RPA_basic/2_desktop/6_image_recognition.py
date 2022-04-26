import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png") #이미지를 현재 화면에서 찾고 정보를 변수에 저장
print(file_menu)
pyautogui.click(file_menu) #file_menu에 저장된 위치 정보의 중간을 클릭함
#pyautogui.click(file_menu.left -200, file_menu.top +200)
# 이렇게 쓰면 x좌표는 file_menu왼쪽기준으로 200만큼 뺀값, y좌표는 위쪽기준으로 200만큼 더한값

trash_icon = pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)
#이미지를 못찾으면 None으로 출력

#같은 이미지가 여러개일 경우
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    pyautogui.click(i)


#속도 개선
#1. GrayScale, 약 30%빨라지지만 정확도 떨어질수있음
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

#2. 범위 지정
#trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x,y,width,height))
#pyautogui.moveTo(trash_icon)

#3. 정확도 조정
#trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.9) #90%일치하면 인식
#pyautogui.moveTo(trash_icon)


#자동화 대상이 바로 보여지지 않는 경우
#1. 계속 기다리기
file_note = pyautogui.locateOnScreen("file_note.png")

while file_note is None:
    file_note = pyautogui.locateOnScreen("file_note.png")
pyautogui.click(file_note)

#2. 일정 시간동안 기다리기(Timeout)
import time
import sys

timeout= 10 #10초 대기
start= time.time() #시작 시간 설정
file_note = None
while file_note is None:
    file_note = pyautogui.locateOnScreen("file_note.png")
    end= time.time() #종료 시간 설정
    if end- start > timeout: #지정한 10초를 초과하면
        print("시간 종료")
        sys.exit()
pyautogui.click(file_note)

#함수 두개로 정의
def find_target(img_file, timeout=30):
    start=time.time()
    target=None
    while target is None:
        target= pyautogui.locateOnScreen(img_file)
        end= time.time()
        if end-start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target= find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s Target not found ({img_file}). Terminate program")
        sys.exit()

