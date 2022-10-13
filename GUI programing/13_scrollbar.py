from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill="y" : y방향으로 채우기

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extened", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1 ~ 31 일                         # 스크롤 움직인 후 위치 고정
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤바 리스트 박스 매핑

root.mainloop()
