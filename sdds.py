from tkinter import *

def set_titlebar_color(root, color):
    # Tkinter 스타일 생성
    style = Style()
    
    # 창의 제목 바 배경색을 설정할 스타일 요소 생성
    style.element_create("titlebar", "from", "default")
    
    # 스타일에 배경색 설정
    style.layout("TButton", [("titlebar", {"sticky": "nswe"})])
    style.configure("TButton", background=color, font=("Arial", 12))

    # 스타일을 창에 적용
    root.title("")
    root.tk_setPalette(background=color)

root = Tk()
root.geometry("400x300")
root.title("창의 제목 바 배경색 설정")

# 창의 제목 바 배경색 설정 (예: 빨간색)
set_titlebar_color(root, "red")

label = Label(root, text="제목 바 배경색을 설정하려면 이 창의 제목 바 배경색이 빨간색으로 변경됩니다.", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
