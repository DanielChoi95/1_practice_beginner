import keyboard
from PIL import ImageGrab
import time


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) #ex) image_20220412_100630.png


keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc") #사용자가 esc를 누를때까지 프로그램 수행


#-------AUTO SCREENSHOT-------------
# import time
# from PIL import ImageGrab

# time.sleep(5) #5초 대기

# for i in range(1,11):
#     #2초 간격으로 10개 이미지 저장
#     img = ImageGrab.grab() #현재 스크린의 이미지를 가져옴
#     img.save("image{}.png".format(i))
#     time.sleep(2) #2초 단위