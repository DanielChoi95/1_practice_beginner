from tkinter import *
import os

root = Tk()

root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표
root.resizable(True, True) #창 크기 변경 불가

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일 있으면 True
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) #1번째 라인, 0 인덱스의 값부터 끝까지 텍스트 가져옴 -> 파일에 씀

menu= Menu(root)

#파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

#기타 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

#스크롤 바

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#텍스트
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True, side="left") #공간 꽉채우기
scrollbar.config(command=txt.yview)


root.mainloop()
