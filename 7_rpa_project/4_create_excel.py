from account import *
from imap_tools import MailBox
import smtplib
from email.message import EmailMessage
from openpyxl import Workbook

applicant_list=[]
#메일 다 받아오기
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #특정 날짜 이후의 메일
    index= 1
    for msg in mailbox.fetch('(SENTSINCE 24-Apr-2022)'): 
        if "파이썬 특강 신청합니다." in msg.subject:
            msg.text1= msg.text[0:8]
            nickname, phone= msg.text1.strip().split("/")
            applicant_list.append((msg, index, nickname, phone))
            index += 1    

#메일 쓰기    
max_val= 3 
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_address = applicant[0].from_ #수신 메일 주소
        # index= applicant[1]
        # nickname= applicant[2]
        # phone= applicant[3]
        index, nickname, phone= applicant[1:]

        title= None
        content= None

        if index <= max_val:
            title= "파이썬 특강 안내 [선정]"
            content= "{}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {}번".format(nickname, index)
        else:
            title= "파이썬 특강 안내 [탈락]"
            content= "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {}번".format(nickname, index-max_val)

        msg= EmailMessage()
        msg["Subject"] = title
        msg["From"]= EMAIL_ADDRESS
        msg["To"]= to_address
        msg.set_content(content)
        smtp.send_message(msg)

#선정자 명단 파일 생성
wb= Workbook()
ws= wb.active
ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_val]:
    ws.append(applicant[1:])
    # index= applicant[1]
    # nickname= applicant[2]
    # phone= applicant[3]
    # ws.append([index, nickname, phone])

wb.save("result.xlsx")

print("모든 작업이 완료되었습니다.")