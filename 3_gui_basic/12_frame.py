from tkinter import *


root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeseburger").pack()
Button(frame_burger, text="Chickenburger").pack()

frame_drink = LabelFrame(root, text="Drinks")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()
