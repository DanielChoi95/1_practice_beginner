#파일 기본
import os
# print(os.getcwd()) #current working directory
# os.chdir("rpa_basic") #rpa_basic으로 작업공간 이동
# print(os.getcwd())
# os.chdir("..") #상위 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") #상위의 상위폴더로 이동
# print(os.getcwd())
# os.chdir("C:/") #주어진 절대 경로로 이동

#파일 경로 만들기
#file_path= os.path.join(os.getcwd(), "my_file.txt") #절대 경로 생성

#파일 경로에서 폴더 정보 가져오기
#print(os.path.dirname(r"C:\Users\user\Desktop\PythonWorkspace\my_file.txt")) #r을 쓰면 탈출문자 x

#파일 정보 가져오기
import time
import datetime

#파일의 생성 날짜(create)
# file_path= "file_note.png"
# ctime = os.path.getctime(file_path)
# print(ctime)
# #날짜 정보를 strftime을 통해서 예쁘게 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# #파일의 수정 날짜(modify)
# mtime= os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# #파일의 마지막 접근 날짜(access)
# atime= os.path.atime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# #파일 크기
# size= os.path.getsize(file_path)
# print(size) #바이트 단위로

#파일 목록 가져오기
# print(os.listdir()) #현재 폴더의 하위 폴더,파일목록 가져오기
# print(os.listdir("rpa_basic")) #주어진 폴더의 하위 폴더,파일목록 가져오기

# #파일 목록 가져오기 (모든 하위 폴더 포함)
# result= os.walk("rpa_basic") #주어진 폴더의 모든 하위 폴더, 파일목록 가져오기
# #현재 폴더로 하려면 "."

# for root, dirs, files in result:
#     print(root, dirs, files)

#만약 폴더 내에서 특정 파일들을 찾으려면?
# name= "11_file_system.py"
# result= []
# for root, dirs, files in os.walk("."): #현재 경로밑으로 다 뒤짐
#     if name in files: #name에 있는 파일을 찾으면
#         result.append(os.path.join(root, name)) #현재경로+파일이름을 result 리스트에 추가
# print(result)

#만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
#ex) *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern= "file*.png" #file로 시작하고 .png로 끝나는 모든 파일
# result= []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): #이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))
# print(result)

#주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("rpa_basic")) #True
# print(os.path.isfile("rpa_basic")) #False

# #만약 지정된 경로에 해당하는 파일이나 폴더가 없다면?
# print(os.path.isfile("noway.png")) #False

# #주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("존재함")
# else:
#     print("존재x")

#파일 만들기
# open("new_file.txt", "a").close() #빈 파일 생성

# #파일명 변경하기
# os.rename("new_file.txt", "renamed_file.txt") #원래이름, 변경할이름

# #파일 삭제하기
# os.remove("renamed_file.txt")

#폴더 만들기
# os.mkdir("new_folder") #현재 경로기준으로 폴더 생성, 이미 있다면 에러발생
# os.mkdir("C:/Users/user/Desktop/PythonWorkspace/old_folder") #절대 경로 기준으로 폴더 생성

# #하위 폴더를 가지는 폴더 생성
# os.makedirs("new_folders/a/b/c")

#폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# #폴더 삭제하기
# os.rmdir("new_folder_rename") #내용물이 있으면 삭제 불가

import shutil #shell utilities
# shutil.rmtree("new_folders") #내용물이 있어도 완전 삭제 가능

#파일 복사하기
#어떤 파일을 폴더 안을 복사하기
# shutil.copy("file_note.png", "test_folder") #원본파일 경로, 대상 폴더 경로
# shutil.copy("file_note.png", "test_folder/copied_file_note.png") #원본파일 경로, 대상 경로(이름 변경)
# shutil.copyfile("file_note.png", "test_folder/copied_file_note2.png") #원본파일 경로, 대상 '파일' 경로
# shutil.copy2("file_note.png", "test_folder/copy2.png") #원본 파일 경로, 대상 폴더 경로
# #copy, copyfile : 메타정보 복사 x (생성날짜 같은거)
# #copy2 : 메타정보 복사 o

#폴더 복사하기
shutil.copytree("test_folder", "test_folder2") #원본 폴더 경로, 대상 폴더 경로 / 내용물도 싹다 복사

#폴더 이동하기
shutil.move("test_folder", "test_folder2") #대상폴더가 없으면 폴더명이 변경되는 효과