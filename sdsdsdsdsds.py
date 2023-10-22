def press():
    global input_text
    input_text = entry1.get()
    label2.configure(text="input_text")
from tkinter import *
window = Tk()
window.geometry("200x300")
label1 = Label(window,text="Add a task:")
# txt = Text(window,width="200",height="2")
button1 = Button(window,text="Add Task")
entry1 = Entry(window,width="200")
label2=Label(window,text="")
label1.pack()
# txt.pack()
entry1.pack()
button1.pack()
label2.pack()
window.mainloop()