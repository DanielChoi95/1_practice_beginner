from tkinter import *

root = Tk()

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

#텍스트
txt = Text(root, width=30, height=5) #텍스트 위젯
txt.pack()
txt.insert(END, "글자를 입력하세요")

#엔트리
e = Entry(root, width=30) #엔터 불가능한 텍스트 위젯 (예 : 로그인창)
e.pack()
e.insert(0, "한줄만 입력하세요")


def btncmd():
    #내용출력
    print(txt.get("1.0", END)) #1 : 첫번쨰 라인, 0:0번째 column 위치
    print(e.get())
    
    #내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn= Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
