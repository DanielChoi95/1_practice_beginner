import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

# #progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate") #좌우로 왔다갔다 함
# progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate") #좌에서 우로 감

# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop() #작동 중지 #프로그레스 바 초기화

# btn= Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기
        p_var2.set(i)  #progress bar의 값 설정
        progressbar2.update() #ui업데이트
        print(p_var2.get())

btn= Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
