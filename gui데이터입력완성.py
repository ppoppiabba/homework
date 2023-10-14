import sqlite3

con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(15), email char(15), birthyear int)")

while (True):
    data1 = input("사용자ID==>")
    if data1=="":
        break
    data2 = input("사용자이름==>")
    data3= input("이메일==>")
    data4 = input("출생연도==>")
    sql = "INSERT INTO userTable VALUES('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()

import sqlite3
con,cur = None,None
data1,data2,data3,data4 = "","","",""
row = None

con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
cur = con.cursor()
cur.execute("SELECT * FROM userTable")
print("사용자ID    사용자이름   이메일                  출생연도")
print("----------------------------------------------------------------------")

while True:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %15s   %5s" % (data1,data2,data3,data4))
con.close()


import sqlite3
from tkinter import * 
from tkinter import messagebox

def insertdata():
    con,cur = None,None
    data1,data2,data3,data4 = "","","",""
    sql = ""
    con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try :
        sql = "INSERT INTO userTable VALUES('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
        cur.execute(sql)
    except:
        messagebox.showerror('오류','데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공','데이터 입력 성공')
    con.commit()
    con.close()

def showdata():
    strdata1,strdata2,strdata3,strdata4 = [],[],[],[]
    con = sqlite3.connect("C:/Users/gram/Desktop/md202310638")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    strdata1.append("사용자ID")
    strdata2.append("사용자이름")
    strdata3.append("이메일")
    strdata4.append("출생연도")
    #strdata1.append("----------")
    #strdata2.append("----------")
    #strdata3.append("----------")
    #strdata4.append("----------")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        strdata1.append(row[0])
        strdata2.append(row[1])
        strdata3.append(row[2])
        strdata4.append(row[3])
    listdata1.delete(0, listdata1.size()-1)
    listdata2.delete(0, listdata1.size()-1)
    listdata3.delete(0, listdata1.size()-1)
    listdata4.delete(0, listdata1.size()-1)
    for item1,item2,item3,item4 in zip(strdata1,strdata2,strdata3,strdata4):
        listdata1.insert(END, item1)
        listdata2.insert(END, item2)
        listdata3.insert(END, item3)
        listdata4.insert(END, item4)
    con.close()
window = Tk()
window.title("GUI 데이터 입력")
edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM,fill = BOTH, expand=1)
edt1 = Entry(edtFrame,width=10); edt1.pack(side=LEFT,padx=10,pady=10)
edt2 = Entry(edtFrame,width=10); edt2.pack(side=LEFT,padx=10,pady=10)
edt3 = Entry(edtFrame,width=10); edt3.pack(side=LEFT,padx=10,pady=10)
edt4 = Entry(edtFrame,width=10); edt4.pack(side=LEFT,padx=10,pady=10)

button1 = Button(edtFrame, text="입력",command= insertdata)
button1.pack(side=LEFT,padx=10,pady=10)
button2 = Button(edtFrame,text="조회",command=showdata)
button2.pack(side=LEFT,padx=10,pady=10)

listdata1 = Listbox(listFrame, bg = 'yellow');
listdata1.pack(side=LEFT, fill = BOTH, expand=1)
listdata2 = Listbox(listFrame,bg = 'yellow')
listdata2.pack(side=LEFT, fill = BOTH, expand=1)
listdata3 = Listbox(listFrame,bg = 'yellow')
listdata3.pack(side=LEFT, fill = BOTH, expand=1)
listdata4 = Listbox(listFrame,bg = 'yellow')
listdata4.pack(side=LEFT, fill = BOTH, expand=1)
window.mainloop()



