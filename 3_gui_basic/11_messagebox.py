from tkinter import *
import tkinter.messagebox as msgbox

root = Tk() #창 생성

root.title("CDH GUI")
root.geometry("640x480") #가로 x 세로 + x좌표 + y좌표

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("Warning", "Sold out")

def error():
    msgbox.showerror("error", "error with transit")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?")
    #네 : 저장 후 종료
    #아니오 : 저장 하지 않고 종료
    #취소 : 프로그램 종료를 취소 
    print("응답:", response) #True, False, None -> 예 1, 아니오 0 , 그 외
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="error").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()
