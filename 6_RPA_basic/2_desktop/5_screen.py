import pyautogui

#스크린 샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png")

pixel = pyautogui.pixel(100, 100)
print(pixel) #좌표값의 rgb값을 알려줌

#좌표값의 rgb와 입력한 rgb가 같은지 알려줌
print(pyautogui.pixelMatchesColor(100,100, (100,100,100)))
#print(pyautogui.pixelMatchesColor(100,100, pixel))
