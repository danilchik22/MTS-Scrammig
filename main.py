import mts
from tkinter import *

from ByFlat import ByFlat
from house import House


def house_click():
    house = House(txt_house.get())
    house.house()


def flat_click():
    Flat = ByFlat(txt_flat.get())
    Flat.flat()

window = Tk()
window.title("Добро пожаловать в приложение Антилистовочник")
window.geometry('600x400')
lbl = Label(window, text = "Введи адрес для визуализации(либо дом рядом): ", font=("Arial Bold", 14))
lbl.grid(column=0, row = 0)
txt_house = Entry(window, width = 40)
txt_house.grid(column=0, row = 1)
txt_house.focus()
btn = Button(window, text = "Запустить визуализацию", fg = "red", command=house_click)
btn.grid(column=0, row = 2)
lbl_flat = Label(window, text = "Введи адрес для поквартирного обхода(либо рядом с ним): ", font=("Arial Bold", 14))
lbl_flat.grid(column= 0, row = 3)
txt_flat = Entry(window, width = 40)
txt_flat.grid(column=0, row = 4)
btn = Button(window, text = "Запустить поквартирный обход", fg = "red", command=flat_click)
btn.grid(column=0, row = 6)
lbl_ps = Label(window, text = "\n\n\n\nP.S. Пока что программа выполняет по одному дому на визуализацию и поквартирный обход.\n"
                              "Если в списке на отработку будет указано больше одного, она отработает некорректно")
lbl_ps.grid(column=0, row = 15)
window.mainloop()



