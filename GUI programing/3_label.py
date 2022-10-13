from cProfile import label
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text="안녕하세요")
label1.pack() # 레이블

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack() # 이미지 레이블

def change():
    label1.config(text="또 만나요") # 레이블 수정
    
    global photo2 # 전역변수
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2) # 이미지 수정

btn = Button(root, text="클릭", command=change)
btn.pack() # 출력 바꾸기

root.mainloop()