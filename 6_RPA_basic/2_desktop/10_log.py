import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# #로그 레벨 네임 : debug < info < warning < error < critical
# #level=logging.ERROR로 하면 error랑 critical만 뜸
# logging.debug("호에에엥")
# logging.info("자동화 수행 준비")
# logging.warning("오래된 스크립트")
# logging.error("삐용삐용")
# logging.critical("장비를 정지합니다 어 안되잖아")

#터미널과 파일에 함께 로그 남기기
logFormatter= logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") #시간 [로그레벨] 메시지
logger= logging.getLogger()

#로그레벨 설정
logger.setLevel(logging.DEBUG)

#스트림 (터미널)
streamHandler= logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#파일
filename= datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler= logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("테스트 진행")