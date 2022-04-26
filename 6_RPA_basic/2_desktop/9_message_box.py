import pyautogui

# pyautogui.countdown(3)
# print("자동화 시작")

pyautogui.alert("자동화 수행 실패", "삐용삐용") #확인버튼만 있는 팝업

result = pyautogui.confirm("계속 진행하시겠습니까?", "확인") #확인 취소 버튼
print(result) #확인누르면 OK 취소누르면 Cancel

result= pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력해줭") #사용자 입력
#취소누르면 None
result= pyautogui.password("암호를 입력하세요", "암호") #암호 입력

#구글에 pyautogui 검색하면 더 공부