from account import *
from imap_tools import MailBox

applicant_list=[]
#메일 다 받아오기
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #특정 날짜 이후의 메일
    index= 1
    for msg in mailbox.fetch('(SENTSINCE 24-Apr-2022)'): 
        if "파이썬 특강" in msg.subject:
            msg.text1= msg.text[0:8]
            nickname, phone= msg.text1.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1
            