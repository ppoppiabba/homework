from tkinter import *

strings = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
current_index = 0  

def update_label():
    global current_index
    label.config(text=strings[current_index])

def next_string():
    global current_index
    current_index = (current_index + 1) % len(strings)
    update_label()

def prev_string():
    global current_index
    current_index = (current_index - 1) % len(strings)
    update_label()

window = Tk()
window.title("tk")

frame = Frame(window)
frame.pack()

prev_button = Button(frame, text="<<이전", command=prev_string)
prev_button.pack(side=LEFT, padx=10)

label = Label(frame, text=strings[current_index], fg="blue", font=("", 20))
label.pack(side=LEFT, padx=10)

next_button = Button(frame, text="다음>>", command=next_string)
next_button.pack(side=LEFT, padx=10)

window.mainloop()
