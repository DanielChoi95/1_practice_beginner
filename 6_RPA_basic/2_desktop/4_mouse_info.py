import pyautogui
#pyautogui.mouseInfo() #마우스 좌표, 컬러 등 정보 프로그램 실행

#모든 동작에 1초씩 sleep 적용
pyautogui.PAUSE = 1

for i in range(10):
    pyautogui.move(100,100)
    #pyautogui.sleep(1)

#마우스 자동화 동작 수행중일때 중단하고 싶으면 마우스를 4 귀퉁이중 하나에 갖다놓으면 됨
#이 기능을 끄고 싶으면 pyautogui.FAILSAFE = False