from tkinter import *
import os


def update():
    global L
    index = MAIN.curselection()[0]  # смотрит какой элемент выбран
    name = L[index]  # узнает имя выбранного элемента по индексу
    newPath = path + ':\\' + name  # создает новый путь с учетом прошлого элемента
    os.chdir(newPath)  # меняет рабочий каталог
    L.clear()  # очищает список с папками
    L = os.listdir()  # смотрит папки в папке
    size = MAIN.size()
    MAIN.delete(0, size)  # удаляет все и listbox
    for i in L:
        MAIN.insert(END, i)  # вставляет новые значения в listbox


root = Tk()

root.geometry('500x500')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2.5
root.wm_geometry("+%d+%d" % (x, y))

MAIN = Listbox(root, selectmode=EXTENDED)

scrollMAIN = Scrollbar(root, command=MAIN.yview)
MAIN.configure(yscrollcommand=scrollMAIN.set)
MAIN.place(x=0, y=50, height=450, width=500)
scrollMAIN.pack(side=RIGHT, fill=Y)

button = Button(root, text='Открыть', command=update)
button.place(x=0, y=20)

label = Label(root)
label.place(x=0, y=0)

path = 'C'
os.chdir('C:\\')  # работаем с диском d
L = os.listdir()  # смотрит папки на диске

for i in L:
    MAIN.insert(END, i)  # вставляет папки на диске d в listbox

root.mainloop()