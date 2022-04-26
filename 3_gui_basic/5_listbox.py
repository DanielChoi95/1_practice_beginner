from tkinter import *

root = Tk()

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) #selectmode= single, extended... height = 리스트박스의 크기
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") #END로 넣으면 현재 항목의 마지막줄에 추가
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(END) 맨 뒤 항목을 삭제, 0 일시 첫번째 항목을 삭제

    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    #선택된 항목 확인(인덱스로 반환)
    print("선택된 항목 : ", listbox.curselection())


btn= Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
