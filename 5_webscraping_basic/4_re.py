import re

p = re.compile("ca.e") 
# . 은 하나의 문자를 의미
# ^ 은 문자열의 시작 ex) (^de) -> destination, desk (O) / fade (x)
# $ 은 문자열의 끝 ex) (se$) -> case, base (O) / face(x)

def print_match(m):

    if m:
        print(m.group()) #일치하는 문자열을 반환
        print(m.string) #입력받은 문자열을 반환
        print(m.start()) #일치하는 문자열의 시작 index
        print(m.end()) #일치하는 문자열의 끝 index
        print(m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m=p.match("case") #match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m) #print(m.group()) 매치되지 않으면 에러가 발생

#m=p.search("good care") #search : 주어진 문자열 중에 일치하는지 확인


# list=p.findall("good careless") #findall : 일치하는 모든 것을 리스트 형태로 반환
# print(list)

