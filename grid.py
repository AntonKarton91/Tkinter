from functions import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Notebook





def get_box():
    # length=l_length.get()
    if ent_length.get():
        return ent_length.get()


win = tk.Tk()
tabs_control=Notebook(win)
tab1=tk.Frame(tabs_control)
tab2=tk.Frame(tabs_control)
tabs_control.pack(fill='both')

tabs_control.add(tab1, text='Расчет гофрокороба')
tabs_control.add(tab2, text='Жесткая упаковка')

fontExample = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
# logo=tk.PhotoImage(file='logo.png')
# win.iconphoto(False,logo)
win.title('ДКО')
win.geometry('500x500+20+20')

tk.Label(master=tab1, text='Расчет коробки', font=fontExample).pack()

tk.Label(text='Габариты изделия:', font=fontExample).place(relx=0.05, rely=0.15)
l_length = tk.Label(text='Длина изделия').place(relx=0.05, rely=0.2)
l_width = tk.Label(text='Ширина изделия').place(relx=0.05, rely=0.25)
l_height = tk.Label(text='Высота изделия').place(relx=0.05, rely=0.3)
ent_length = tk.Entry()
ent_width = tk.Entry()
ent_height = tk.Entry()

ent_length.place(relx=0.4, rely=0.2)
ent_width.place(relx=0.4, rely=0.25)
ent_height.place(relx=0.4, rely=0.2)

l_skin_type = tk.Label(text='Вид пленки:', font=fontExample).place(relx=0.05, rely=0.35)

r_var = tk.BooleanVar()
r_var.set(0)
r1 = tk.Radiobutton(text='Без пленки',
                 variable=r_var, value=0)
r2 = tk.Radiobutton(text='Стрейч',
                 variable=r_var, value=1)
r3 = tk.Radiobutton(text='ВПП',
                 variable=r_var, value=2)

r1.place(relx=0.05, rely=0.4)
r2.place(relx=0.25, rely=0.4)
r3.place(relx=0.45, rely=0.4)



l_skin_type = tk.Label(text='Параметры упаковки и паллеты:', font=fontExample).place(relx=0.05, rely=0.45)

tk.Label(text='Размер листа картона').place(relx=0.05, rely=0.5)
ent_sheetX = tk.Entry(width=6)
ent_sheetX.insert(0,'2100')
tk.Label(text='x').place(relx=0.45, rely=0.5)
ent_sheetY = tk.Entry(width=6)
ent_sheetY.insert(0,'1400')

ent_sheetX.place(relx=0.35, rely=0.5)
ent_sheetY.place(relx=0.5, rely=0.5)

tk.Label(text='Размер палеты').place(relx=0.05, rely=0.55)
ent_palletX = tk.Entry(width=6)
ent_palletX.insert(0,'1200')
tk.Label(text='x').place(relx=0.45, rely=0.55)
ent_palletY = tk.Entry(width=6)
ent_palletY.insert(0,'800')
tk.Label(text='x').place(relx=0.6, rely=0.55)
ent_palletZ = tk.Entry(width=6)
ent_palletZ.insert(0,'1800')

ent_palletX.place(relx=0.35, rely=0.55)
ent_palletY.place(relx=0.5, rely=0.55)
ent_palletZ.place(relx=0.65, rely=0.55)

tk.Label(text='Размер свеса палеты').place(relx=0.05, rely=0.6)
ent_pallet_overhang = tk.Entry(width=6)
ent_pallet_overhang.insert(0,'0')
ent_pallet_overhang.place(relx=0.4, rely=0.6)

but1=tk.Button(text='Расчитать', command=get_box)
but1.place(relx=0.1, rely=0.65)

tk.Label(text='Количество коробок в листе:').place(relx=0.05, rely=0.7)
tk.Label(text=f'{get_box}').place(relx=0.3, rely=0.7)



win.mainloop()
