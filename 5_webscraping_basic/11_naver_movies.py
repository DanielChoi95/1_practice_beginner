import requests
import re
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}


url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=2021%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs = {"class":"thumb"})
#print(images)

for idx, image in enumerate(images):
    print(image["src"])
    #image_url = image["src"] ##################
    if image_url.startswith("//"):
        image_url = "https:" +image_url

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)
        