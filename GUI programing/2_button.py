from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() # 버튼 출력하기 위해

btn2 = Button(root, padx=10, pady=5, text="버튼2")
btn2.pack() # padx : 가로 공간(여백) , pady : 세로 공간(여백)

btn3 = Button(root, padx=5, pady=10, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4")
btn4.pack() # width : 가로 , height : 세로

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack() # fg : 글씨 색 , bg : 배경 색

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack() # 이미지로 버튼 만들기

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
