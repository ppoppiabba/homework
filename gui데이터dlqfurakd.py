import sqlite3
from tkinter import *
from tkinter import messagebox

def insertdata():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""
    con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
    cur = con.cursor()

    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    try:
        sql = "INSERT INTO userTable VALUES(?,?,?,?)"
        cur.execute(sql, (data1, data2, data3, data4))
    except:
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else:
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()

def showdata():
    con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()

    listdata1.delete(0, END)
    listdata2.delete(0, END)
    listdata3.delete(0, END)
    listdata4.delete(0, END)

    for row in rows:
        listdata1.insert(END, row[0])
        listdata2.insert(END, row[1])
        listdata3.insert(END, row[2])
        listdata4.insert(END, row[3])
    con.close()

window = Tk()
window.title("GUI 데이터 입력")
edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

button1 = Button(edtFrame, text="입력", command=insertdata)
button1.pack(side=LEFT, padx=10, pady=10)
button2 = Button(edtFrame, text="조회", command=showdata)
button2.pack(side=LEFT, padx=10, pady=10)

listdata1 = Listbox(listFrame, bg='yellow')
listdata1.pack(side=LEFT, fill=BOTH, expand=1)
listdata2 = Listbox(listFrame, bg='yellow')
listdata2.pack(side=LEFT, fill=BOTH, expand=1)
listdata3 = Listbox(listFrame, bg='yellow')
listdata3.pack(side=LEFT, fill=BOTH, expand=1)
listdata4 = Listbox(listFrame, bg='yellow')
listdata4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
