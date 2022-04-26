import requests

res = requests.get("http://google.com")
res.raise_for_status()
# print("응답코드 :", res.status_code) #200이면 정상, 403은 접근권한x

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
