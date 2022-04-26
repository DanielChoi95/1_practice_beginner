from tkinter import *

root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

def create_new_file():
    print("새로운 파일 생성")

menu = Menu(root)

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(labe="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가 (라디오 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language", menu=menu_lang)

#View 메뉴 (체크 버튼)
menu_view=Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)

root.mainloop()
