from tkinter import *

window = Tk()
window.title("애완동물 선택하기")

label1 = Label(window, text="좋아하는 동물 투표", font=("궁서체",), fg="blue")
label1.pack()

def showImage():
    selected_animal = var.get()
    animal_images = {
        1: "C:\\Users\\gram\\Desktop\\dog.gif",
        2: "C:\\Users\\gram\\Desktop\\cat.gif",
        3: "C:\\Users\\gram\\Desktop\\rabbit.gif",
    }
    selected_image = animal_images.get(selected_animal)

    if selected_image:
        image = PhotoImage(file=selected_image)
        image_label.configure(image=image)
        image_label.image = image
    else:
        image_label.configure(image=None)

var = IntVar()
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)

rb1.pack()
rb2.pack()
rb3.pack()

image_label = Label(window)
image_label.pack()

button1 = Button(window, text="사진보기", command=showImage)
button1.pack()

window.mainloop()
