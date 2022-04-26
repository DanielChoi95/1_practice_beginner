from tkinter import *

root = Tk()

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

chkvar = IntVar() #chkvar에 int 형태로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) #variable은 체크를 했을때의 값을 저장
#chkbox.select() #자동으로 선택 되있음
#chkbox.deselect #자동으로 해제 되있음
chkbox.pack()

chkvar2= IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 숫자 0일시 체크해제, 1일시 체크
    print(chkvar2.get())


btn= Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
