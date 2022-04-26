from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("CDH image merge")
root.resizable(False, False) #창 크기 변경 불가

#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="Select Images",\
         filetypes=(("png", "*.png"), ("All", "*.*")), initialdir=r"C:/")
    
    #사용자가 선택한 파일 목록 출력
    for file in files:
        list_file.insert(END, file)

#파일 선택 삭제
def del_file():
    #인덱스를 앞에서부터 지우면 인덱스가 초기화되기때문에 리버스값을 받아옴(실제로 뒤집지는 않음)
    for index in reversed(list_file.curselection()): 
        list_file.delete(index)

#저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected =='':
        return
    entry_dest_path.delete(0,END)
    entry_dest_path.insert(0, folder_selected)

#이미지 통합 함수
def merge_image():

    try:

        #가로 넓이 옵션 받아오기
        img_width = combo_width.get
        if img_width == "Original":
            img_width = -1
        else:
            img_width = int(img_width)


        #간격 옵션 받아오기
        img_dist = combo_dist.get()
        if img_dist == "Short":
            img_dist = 30
        elif img_dist == "Medium":
            img_dist = 60
        elif img_dist == "Long":
            img_dist = 90
        else:
            img_dist = 0

        #포맷 옵션 받아오기
        img_format = combo_format.get().lower()

        #이미지 사이즈를 리스트에 넣어서 하나씩 옵션에 맞게 처리 중
        image__sizes = [] #(width1, height1), ....
        if img_width > -1: #width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1]/ x.size[0])) for x in images] 
            #높이를 비율에 맞게 변경

        else: #원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]


        images = [Image.open(x) for x in list_file.get(0,END)]
        #Image로 불러온것에는 size정보가 있다 size[0] : width, size[1] : height
        widths, heights = zip(*(image_sizes))  

        #최대 넓이, 전체 높이 구해옴
        max_width, total_height = max(widths), sum(heights)

        #스케치북 준비
        if img_dist > 0:  #이미지 간격 옵션 적용
            total_height += (img_dist * (len(images) -1))


        result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) #흰색 배경
        y_offset = 0 #y 위치 정보

        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1] #height 값 만큼 더해줌

        for idx, img in enumerate(images):
            #width 가 원본유지가 아닐 때는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] +img_dist) #불러온 사진의 다음 자리에 붙이기위해서

            progress = (idx + 1) / len(images) * 100  #실제 퍼센트 정보를 계산
            p_var.set(progress)
            progress_bar.update()

        #포맷 옵션 처리
        file_name = "CDH_Photo." +img_format
        dest_path = os.path.join(entry_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Notice", "Merge has been done")
        
    except Exception as err :#예외 처리
        msgbox.showerror("Error", err)
    

#시작
def start():
    #각 옵션들 값을 확인

    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add Image Files")
        return
    

    #저장 경로 확인
    if len(entry_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select Save Path")
        return

    #이미지 통합 작업
    merge_image()



#파일 프레임 (파일 추가, 선택 삭제)
frame_file = Frame(root)
frame_file.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(frame_file, text="Add Files", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(frame_file, text="Delete Files", padx=5, pady=5, width=12, command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임
frame_list = Frame(root)
frame_list.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(frame_list, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장 경로 프레임
frame_path = LabelFrame(root, text="Save Path")
frame_path.pack(fill="x", padx=5, pady=5, ipady=5)

entry_dest_path = Entry(frame_path)
entry_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #높이 변경

btn_dest_path = Button(frame_path, text="Browse", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

#옵션 프레임
frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5, ipady=5)

#1.가로 넓이 옵션
label_width = Label(frame_option, text="Width", width=8)
label_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
combo_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
combo_width.current(0)
combo_width.pack(side="left", padx=5, pady=5)

#2.간격 옵션
label_dist = Label(frame_option, text="Distance", width=8)
label_dist.pack(side="left", padx=5, pady=5)

opt_dist = ["None", "Short", "Medium", "Long"]
combo_dist = ttk.Combobox(frame_option, state="readonly", values=opt_dist, width=10)
combo_dist.current(0)
combo_dist.pack(side="left", padx=5, pady=5)

#3.파일 포맷 옵션
label_format = Label(frame_option, text="Format", width=8)
label_format.pack(side="left", padx=5, pady=5)

opt_format = ["png", "jpg", "bmp"]
combo_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
combo_format.current(0)
combo_format.pack(side="left", padx=5, pady=5)

#진행 상황 프레임
frame_progress = LabelFrame(root, text="Progression")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#작업 실행 / 취소 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)




root.mainloop()
