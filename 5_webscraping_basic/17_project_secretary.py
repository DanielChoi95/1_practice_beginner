#날씨, 헤드라인 뉴스, IT뉴스, 오늘의 영어 회화

import requests
from bs4 import BeautifulSoup

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%B8%EC%82%B0+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    weather_today = soup.find("div", attrs={"class" : "open"})
    #print(weather_today)
    
    
    summary = weather_today.find_all("p", attr={"class":"summary"})
    # curr_temp = soup.find("div", attr={"class":"temperature_text"}).get_text()
    # min_temp = soup.find("span", attr={"class":"lowest"}).get_text()
    # max_temp = soup.find("span", attr={"class":"highest"}).get_text()
#     rain_rate_am = ''

#     print(summary)
#     print("현재 {} (최저 {} / 최고{})".format(curr_temp, min_temp, max_temp))

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    


# #날씨
if __name__ == "__main__":
    #scrape_weather()
    scrape_headline_news()
