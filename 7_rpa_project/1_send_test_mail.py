import smtplib
from account import *
from email.message import EmailMessage
from random import *

nicknames= ["주찬양", "이용민", "류래현", "김세현", "박영호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg= EmailMessage()
        msg["Subject"]= "파이썬 특강 신청합니다."
        msg["From"]= EMAIL_ADDRESS
        msg["To"]= "dhyun120@gmail.com"

        content= nickname + "/" + str(randint(1000,9999))
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 메일 발송 완료")