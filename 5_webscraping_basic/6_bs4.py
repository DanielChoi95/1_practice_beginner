import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
#print(soup.a) #soup에 들어있는 전체 소스중에서 a라는 element가 가지고 있는 소스를 가져옴
#print(soup.a.attrs) #a element의 속성 정보(attributes)를 출력
#print(soup.a["href"]) #a element의 특정 속성 값 정보를 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) #class="Nbtn_upload" 인 a element를 찾는다
# print(soup.find(attrs={"class": "Nbtn_upload"})) #class="Nbtn_upload" 인 어떤 element를 찾는다

rank1= soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2= rank1.next_sibling.next_sibling
# rank3= rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
#print(rank1.parent)
rank1.find_next_sibling("li") #빈 껍데기 행이 있을 경우 사용

rank1.find_next_siblings("li")