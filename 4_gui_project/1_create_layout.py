from tkinter import *
import tkinter.ttk as ttk
from turtle import width

root = Tk()
root.title("CDH image joiner")
root.resizable(False, False) #창 크기 변경 불가

#파일 프레임 (파일 추가, 선택 삭제)
frame_file = Frame(root)
frame_file.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(frame_file, text="Add Files", padx=5, pady=5, width=12)
btn_add_file.pack(side="left")

btn_del_file = Button(frame_file, text="Delete Files", padx=5, pady=5, width=12)
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

btn_dest_path = Button(frame_path, text="Browse", width=10)
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
combo_formatt = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
combo_formatt.current(0)
combo_formatt.pack(side="left", padx=5, pady=5)

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

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right", padx=5, pady=5)




root.mainloop()
