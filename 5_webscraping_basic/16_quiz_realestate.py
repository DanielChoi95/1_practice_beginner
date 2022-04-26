import re
from bs4 import BeautifulSoup
import requests


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EB%A7%A4%EB%AC%BC"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#매물 다 불러오기
estates = soup.find_all("tr", attrs = {"class":"_land_tr_row"})

for idx, estate in enumerate(estates):
    columns = estate.find_all("td")

    print("=========== 매물 {} ===========".format(idx+1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[3].get_text(), "(공급/전용)" )
    print("가격 :", columns[4].get_text(), "(만원)")
    print("단지명", columns[2].find("a", attrs = {"class": "link"}).get_text())
    print("층 :", columns[5].get_text())




