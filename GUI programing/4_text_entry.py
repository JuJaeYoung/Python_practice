from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack() # 텍스트 위젯 생성

txt.insert(END, "글자를 입력하세요") # 텍스트 창에 기본 입력 문구

e = Entry(root, width=30)
e.pack() # entry : 한 줄 입력 창 (로그인 등 이용)
e.insert(0,"한 줄만 입력하세요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치, END : 끝까지
    print(e.get()) # entry 내용 출력

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
