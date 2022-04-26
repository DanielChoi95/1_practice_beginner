from tkinter import *


root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 동작 안하고 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i) +"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
