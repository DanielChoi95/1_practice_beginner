import tkinter.ttk as ttk
from tkinter import *

root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택하세요").pack()

#콤보 박스 : 화살표누르고 여러값중 선택하는 박스
values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #목록의 최초 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn= Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
