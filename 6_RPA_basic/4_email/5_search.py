from imap_tools import MailBox
from account import *

# mailbox= MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #전체 메일 다 가져오기
    # for msg in mailbox.fetch(): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM dhyun120@naver.com)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #어떤 글자를 포함하는 메일(제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test mail")'): 
    #     #띄어쓰기로 구분되어 test 또는 mail이 들어간것을 찾음
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #어떤 글자를 포함하는 메일(제목만) / 한글 불가
    # for msg in mailbox.fetch('(SUBJECT "test mail")'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #메일을 가져온 후 제목에 텍스트있는지 확인 (우회하여 한글 가능한 방법)
    # for msg in mailbox.fetch(limit=5, reverse=True): 
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    #특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-NOV-2020)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 07-NOV-2020)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 07-NOV-2020 SUBJECT "test mail" UNSEEN)', limit=5, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #2가지 이상의 조건 중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 07-NOV-2020 SUBJECT "test mail" UNSEEN)', limit=5, reverse=True): 
        print("[{}] {}".format(msg.from_, msg.subject))
    



#구글에 imap tools 검색