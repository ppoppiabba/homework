from tkinter import *
from ttkthemes import ThemedTk

def change_title_background_color():
    window.set_theme("plastik")  # 원하는 테마를 설정합니다.

window = ThemedTk(theme="clearlooks")  # 초기 테마 설정
window.title("타이틀 바 배경색 변경")

label = Label(window, text="윈도우 타이틀 바 배경색을 변경하려면 테마를 선택하세요.")
label.pack(pady=20)

change_button = Button(window, text="테마 변경", command=change_title_background_color)
change_button.pack()

window.mainloop()
