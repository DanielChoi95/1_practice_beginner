import pyautogui

# fw= pyautogui.getActiveWindow() #현재 활성화된 창
# print(fw.title) #창의 제목 정보
# print(fw.size) #창의 크기 정보 width, height
# print(fw.left, fw.top, fw.right, fw.bottom) #창의 좌표 정보
# pyautogui.click(fw.left + 10, fw.top +20)

# for w in pyautogui.getAllWindows():
#     print(w) #모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

w= pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive() == False: #현재 활성화가 되지 않았다면
    w.activate() #활성화

if w.isMaximized() == False: #현재 최대화가 되지 않았다면
    w.maximize() #최대화

w.restore() #화면 원상복귀

w.close() #윈도우 닫기, 저장할 내용있으면 물어봄