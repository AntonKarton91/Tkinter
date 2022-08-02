import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Notebook
from functions import *
import tkinter.messagebox as mb



def get_box():
    if ent_length.get() and ent_width.get() and ent_height.get():
        try:

            a = abs(int(ent_length.get()))
            b = abs(int(ent_width.get()))
            if a<b:
                a,b=b,a
            c = abs(int(ent_height.get()))
            m = abs(int(ent_sheetY.get()))
            n = abs(int(ent_sheetX.get()))
            r = abs(int(r_var.get()))

            lp = abs(int(ent_palletX.get()))
            wp = abs(int(ent_palletY.get()))
            hp = abs(int(ent_palletZ.get()))
            overhang = abs(int(ent_pallet_overhang.get()))

            if getBoxCount(a, b, c, r, m, n):
                res = getBoxCount(a, b, c, r, m, n)
                # print(lp, wp, hp, res[3], res[4], res[5])
                ress = pallet(lp, wp, hp, res[3], res[4], res[5], overhang)
                res1=ress[0]
                res2=ress[1]
                tk.Label(master=tab1, text=f'{res[0]}').place(relx=0.65, rely=0.74, anchor='w')
                tk.Label(master=tab1, text=f'{res[1]}').place(relx=0.65, rely=0.78, anchor='w')
                tk.Label(master=tab1, text=f'{res[2]}').place(relx=0.65, rely=0.82, anchor='w')
                tk.Label(master=tab1, text=f'{res[3]} x {res[4]} x {res[5]}').place(relx=0.65, rely=0.86, anchor='w')
                tk.Label(master=tab1, text=f'{res1}').place(relx=0.65, rely=0.9, anchor='w')
                tk.Label(master=tab1, text=f'{res2[0]}').place(relx=0.3, rely=0.94, anchor='w')
                tk.Label(master=tab1, text=f'{res2[1]}').place(relx=0.6, rely=0.94, anchor='w')
            else:
                msg = "Размер коробки слишком велик".upper()
                mb.showinfo("AHTUNG", msg)
        except:
            msg = "Атата, введи-ка  лучше цифры".upper()
            mb.showinfo("AHTUNG", msg)


def get_rigid():
    if ent_Rlength.get() and ent_Rwidth.get() and ent_Rheight.get():

        try:

            a1 = abs(int(ent_Rlength.get()))
            b1 = abs(int(ent_Rwidth.get()))
            c1 = abs(int(ent_Rheight.get()))
            x1=abs(int(ent_RsheetX1.get()))
            y1=abs(int(ent_RsheetY1.get()))
            x2 = abs(int(ent_RsheetX2.get()))
            y2 = abs(int(ent_RsheetY2.get()))
            if (a1 <= x1 - 106 and b1 <= y1 - 106)  or (a1 <= y1 - 106 and b1 <= x1 - 106):
                res2 = s_count(a1, b1, c1, x1,y1,x2,y2)

                tk.Label(master=tab2, text=f'{res2[0]}').place(relx=0.75, rely=0.75, anchor='w')
                tk.Label(master=tab2, text=f'{res2[1]}').place(relx=0.75, rely=0.8, anchor='w')
                tk.Label(master=tab2, text=f'{res2[5]}').place(relx=0.75, rely=0.85, anchor='w')
                tk.Label(master=tab2, text=f'{res2[2]} x {res2[3]} x {res2[4]}').place(relx=0.7, rely=0.9, anchor='w')

            else:
                msg = "Размер изделия слишком велик".upper()
                mb.showinfo("AHTUNG", msg)
        except:
            msg = "Атата, введи-ка  лучше цифры".upper()
            mb.showinfo("AHTUNG", msg)

lis12 = []
def get_br():
    global lis12
    lis12 = []
    try:
        for i in range(len(lis)):
            if lis[i][1].get() and lis[i][0].get():
                for j in range(int(lis[i][1].get())):
                    lis12.append(lis[i][0].get())
        lis12 = [abs(int(m)) for m in lis12]
        brres = round(brusCalculation1(lis12),3)
        if brres:
            brrez['text'] = f'Количество брусков 25х50х{ent_lBrus.get()}:'
            brrez1['text'] = f'{brres}'

        else:
            msg = "Размер брусков слишком велик".upper()
            mb.showinfo("AHTUNG", msg)
    except:
        msg = "Введи нормально".upper()
        mb.showinfo("AHTUNG", msg)
ry1 = 0.15


def add():
    global count
    if count == 5:
        but3['text'] = 'Куда уж еще?'
    if count == 6:
        but3['text'] = 'Ну ладно,\n еще один'
    if count == 7:
        but3['text'] = 'ЭЭ, тормози'

    if count <= 7:
        global lis
        global ry2, ry1, lBrus
        ry1 += 0.05
        ry2 += 0.05
        tk.Label(master=tab3, text=f'Длина бруска {count + 1}:').place(relx=0.05, rely=ry1, anchor='w')
        tk.Label(master=tab3, text='Количество').place(relx=0.4, rely=ry1, anchor='w')
        lis.append([])
        lis[count + 1].append(tk.Entry(master=tab3, width=10))
        lis[count + 1].append(tk.Entry(master=tab3, width=5))
        lis[count + 1][0].place(relx=0.25, rely=ry1, anchor='w')
        lis[count + 1][1].place(relx=0.55, rely=ry1, anchor='w')
        count += 1

    if count > 7:
        but3['text'] = 'Все, харош'
    lBrus.place(relx=0.05, rely=ry2, anchor='w')
    ent_lBrus.place(relx=0.25, rely=ry2, anchor='w')
    but4.place(relx=0.25, rely=(ry2 + 0.1), anchor='w')
    but5.place(relx=0.4, rely=(ry2 + 0.1), anchor='w')
    brrez.place(relx=0.05, rely=(ry2 + 0.2), anchor='w')
    brrez1.place(relx=0.5, rely=(ry2 + 0.2), anchor='w')


def clear():
    if lis:
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                lis[i][j].delete(0, 'end')
    ent_lBrus.delete(0, 'end')

def clear_tab1():
    ent_length.delete(0, 'end')
    ent_width.delete(0, 'end')
    ent_height.delete(0, 'end')
    r_var.set(0)
    ent_sheetX.delete(0, 'end')
    ent_sheetX.insert(0, '2100')
    ent_sheetY.delete(0, 'end')
    ent_sheetY.insert(0, '1400')
    ent_palletX.delete(0, 'end')
    ent_palletX.insert(0, '1200')
    ent_palletY.delete(0, 'end')
    ent_palletY.insert(0, '800')
    ent_palletZ.delete(0, 'end')
    ent_palletZ.insert(0, '1800')
    ent_pallet_overhang.delete(0, 'end')
    ent_pallet_overhang.insert(0, '0')




win = tk.Tk()
tabs_control = Notebook(win)
tab1 = tk.Frame(tabs_control, height=600)
tab2 = tk.Frame(tabs_control, height=600)
tab3 = tk.Frame(tabs_control, height=600)
tabs_control.pack(fill='both')

tabs_control.add(tab1, text='Расчет гофрокороба')
tabs_control.add(tab2, text='Расчет жесткой упаковки')
tabs_control.add(tab3, text='Расчет хлыста ')

fontExample = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")

win.title('ДКО')
win.geometry('500x600+20+20')

tk.Label(master=tab1, text='Расчет гофрокороба', font=fontExample, width=300).place(relx=0.5, rely=0.04,
                                                                                    anchor='center')

tk.Label(master=tab1, text='Габариты изделия:', font=fontExample).place(relx=0.05, rely=0.1, anchor='w')
l_length = tk.Label(master=tab1, text='Длина изделия').place(relx=0.05, rely=0.15, anchor='w')
l_width = tk.Label(master=tab1, text='Ширина изделия').place(relx=0.05, rely=0.2, anchor='w')
l_height = tk.Label(master=tab1, text='Высота изделия').place(relx=0.05, rely=0.25, anchor='w')
ent_length = tk.Entry(master=tab1)
ent_width = tk.Entry(master=tab1)
ent_height = tk.Entry(master=tab1)

ent_length.place(relx=0.3, rely=0.15, anchor='w')
ent_width.place(relx=0.3, rely=0.2, anchor='w')
ent_height.place(relx=0.3, rely=0.25, anchor='w')

l_skin_type = tk.Label(master=tab1, text='Вид пленки:', font=fontExample).place(relx=0.05, rely=0.325, anchor='w')

r_var = tk.IntVar()
r_var.set(0)
r1 = tk.Radiobutton(master=tab1, text='Без пленки',
                    variable=r_var, value=0)
r2 = tk.Radiobutton(master=tab1, text='Стрейч',
                    variable=r_var, value=1)
r3 = tk.Radiobutton(master=tab1, text='ВПП',
                    variable=r_var, value=2)

r1.place(relx=0.3, rely=0.325, anchor='w')
r2.place(relx=0.5, rely=0.325, anchor='w')
r3.place(relx=0.65, rely=0.325, anchor='w')

l_skin_type = tk.Label(master=tab1, text='Параметры упаковки и паллеты:', font=fontExample) \
    .place(relx=0.05, rely=0.4, anchor='w')

tk.Label(master=tab1, text='Размер листа картона').place(relx=0.05, rely=0.45, anchor='w')
ent_sheetX = tk.Entry(master=tab1, width=6)
ent_sheetX.insert(0, '2100')
tk.Label(master=tab1, text='x').place(relx=0.45, rely=0.45, anchor='w')
ent_sheetY = tk.Entry(master=tab1, width=6)
ent_sheetY.insert(0, '1400')

ent_sheetX.place(relx=0.35, rely=0.45, anchor='w')
ent_sheetY.place(relx=0.5, rely=0.45, anchor='w')

tk.Label(master=tab1, text='Размер палеты').place(relx=0.05, rely=0.5, anchor='w')
ent_palletX = tk.Entry(master=tab1, width=6)
ent_palletX.insert(0, '1200')
tk.Label(master=tab1, text='x').place(relx=0.45, rely=0.5, anchor='w')
ent_palletY = tk.Entry(master=tab1, width=6)
ent_palletY.insert(0, '800')
tk.Label(master=tab1, text='x').place(relx=0.6, rely=0.5, anchor='w')
ent_palletZ = tk.Entry(master=tab1, width=6)
ent_palletZ.insert(0, '1800')

ent_palletX.place(relx=0.35, rely=0.5, anchor='w')
ent_palletY.place(relx=0.5, rely=0.5, anchor='w')
ent_palletZ.place(relx=0.65, rely=0.5, anchor='w')

tk.Label(master=tab1, text='Размер свеса палеты').place(relx=0.05, rely=0.55, anchor='w')
ent_pallet_overhang = tk.Entry(master=tab1, width=6)
ent_pallet_overhang.insert(0, '0')
ent_pallet_overhang.place(relx=0.35, rely=0.55, anchor='w')

but1 = tk.Button(master=tab1, text='Расчитать', command=get_box)
but1.place(relx=0.1, rely=0.625, anchor='w')
butt1 = tk.Button(master=tab1, text='Очистить', command=clear_tab1)
butt1.place(relx=0.25, rely=0.625, anchor='w')

tk.Label(master=tab1, text='Результаты:', font=fontExample).place(relx=0.05, rely=0.7, anchor='w')
tk.Label(master=tab1, text='Количество коробок в листе:').place(relx=0.05, rely=0.74, anchor='w')
tk.Label(master=tab1, text='Длина реза коробки:').place(relx=0.05, rely=0.78, anchor='w')
tk.Label(master=tab1, text='Листов на одну коробку с учетом раскроя:').place(relx=0.05, rely=0.82, anchor='w')
tk.Label(master=tab1, text='Внутренний размер коробки:').place(relx=0.05, rely=0.86, anchor='w')
tk.Label(master=tab1, text='Количество коробок на паллете:').place(relx=0.05, rely=0.9, anchor='w')
tk.Label(master=tab1, text='По дну паллета:').place(relx=0.05, rely=0.94, anchor='w')
tk.Label(master=tab1, text='В высоту:').place(relx=0.4, rely=0.94, anchor='w')




tk.Label(master=tab2, text='Расчет жесткой упаковки', font=fontExample, width=300).place(relx=0.5, rely=0.04,
                                                                                         anchor='center')


def clear_tab2():
    ent_Rlength.delete(0, 'end')
    ent_Rwidth.delete(0, 'end')
    ent_Rheight.delete(0, 'end')
    ent_RsheetX1.delete(0, 'end')
    ent_RsheetX1.insert(0, '2745')
    ent_RsheetY1.delete(0, 'end')
    ent_RsheetY1.insert(0, '1220')
    ent_RsheetX2.delete(0, 'end')
    ent_RsheetX2.insert(0, '2440')
    ent_RsheetY2.delete(0, 'end')
    ent_RsheetY2.insert(0, '1220')




tk.Label(master=tab2, text='Габариты изделия:', font=fontExample).place(relx=0.05, rely=0.1, anchor='w')
l_Rlength = tk.Label(master=tab2, text='Длина изделия').place(relx=0.05, rely=0.15, anchor='w')
l_Rwidth = tk.Label(master=tab2, text='Ширина изделия').place(relx=0.05, rely=0.2, anchor='w')
l_Rheight = tk.Label(master=tab2, text='Высота изделия').place(relx=0.05, rely=0.25, anchor='w')
ent_Rlength = tk.Entry(master=tab2)
ent_Rwidth = tk.Entry(master=tab2)
ent_Rheight = tk.Entry(master=tab2)

ent_Rlength.place(relx=0.3, rely=0.15, anchor='w')
ent_Rwidth.place(relx=0.3, rely=0.2, anchor='w')
ent_Rheight.place(relx=0.3, rely=0.25, anchor='w')

tk.Label(master=tab2, text='Параметры упаковки:', font=fontExample) \
    .place(relx=0.05, rely=0.35, anchor='w')

tk.Label(master=tab2, text='Размер листа материала на стенки и верх:').place(relx=0.05, rely=0.4, anchor='w')
ent_RsheetX1 = tk.Entry(master=tab2, width=6)
ent_RsheetX1.insert(0, '2745')
tk.Label(master=tab2, text='x').place(relx=0.65, rely=0.4, anchor='w')
ent_RsheetY1 = tk.Entry(master=tab2, width=6)
ent_RsheetY1.insert(0, '1220')

ent_RsheetX1.place(relx=0.55, rely=0.4, anchor='w')
ent_RsheetY1.place(relx=0.7, rely=0.4, anchor='w')

tk.Label(master=tab2, text='Размер листа материала на основание:').place(relx=0.05, rely=0.45, anchor='w')
ent_RsheetX2 = tk.Entry(master=tab2, width=6)
ent_RsheetX2.insert(0, '2440')
tk.Label(master=tab2, text='x').place(relx=0.65, rely=0.45, anchor='w')
ent_RsheetY2 = tk.Entry(master=tab2, width=6)
ent_RsheetY2.insert(0, '1220')

ent_RsheetX2.place(relx=0.55, rely=0.45, anchor='w')
ent_RsheetY2.place(relx=0.7, rely=0.45, anchor='w')

but2 = tk.Button(master=tab2, text='Расчитать', command=get_rigid)
but2.place(relx=0.1, rely=0.525, anchor='w')
but2 = tk.Button(master=tab2, text='Очистить', command=clear_tab2)
but2.place(relx=0.25, rely=0.525, anchor='w')


tk.Label(master=tab2, text='Результаты:', font=fontExample).place(relx=0.05, rely=0.7, anchor='w')
tk.Label(master=tab2, text='Количество брусков 25х50х3000:').place(relx=0.05, rely=0.75, anchor='w')
tk.Label(master=tab2, text='Количество листов 3 мм:').place(relx=0.05, rely=0.8, anchor='w')
tk.Label(master=tab2, text='Количество листов 9 мм:').place(relx=0.05, rely=0.85, anchor='w')
tk.Label(master=tab2, text='Размер жесткой упаковки:').place(relx=0.05, rely=0.9, anchor='w')

lis = []
ry = 0.15
ry2 = 0.25
count = 0
tk.Label(master=tab3, text='Расчет количества хлыстов', font=fontExample, width=300).place(relx=0.5, rely=0.04,
                                                                                           anchor='center')
tk.Label(master=tab3, text='Параметры:', font=fontExample).place(relx=0.05, rely=0.1, anchor='w')
tk.Label(master=tab3, text='Длина бруска 1:').place(relx=0.05, rely=ry, anchor='w')
tk.Label(master=tab3, text='Количество:').place(relx=0.4, rely=ry, anchor='w')
lis.append([])
lis[0].append(tk.Entry(master=tab3, width=10))
lis[0].append(tk.Entry(master=tab3, width=5))

lis[0][0].place(relx=0.25, rely=0.15, anchor='w')
lis[0][1].place(relx=0.55, rely=0.15, anchor='w')

but3 = tk.Button(master=tab3, text='Добавить', command=add, width=10, height=3)
but3.place(relx=0.7, rely=0.2, anchor='w')

lBrus = tk.Label(master=tab3, text='Длина хлыста:')
lBrus.place(relx=0.05, rely=ry2, anchor='w')
ent_lBrus = tk.Entry(master=tab3, width=10)
ent_lBrus.place(relx=0.25, rely=ry2, anchor='w')

but4 = tk.Button(master=tab3, text='Расчитать', command=get_br)
but4.place(relx=0.25, rely=0.35, anchor='w')

but5 = tk.Button(master=tab3, text='Очистить', command=clear)
but5.place(relx=0.4, rely=0.35, anchor='w')



brrez = tk.Label(master=tab3, text='Количество брусков 25х50х...:')
brrez.place(relx=0.05, rely=0.45, anchor='w')

brrez1 = tk.Label(master=tab3, text=' ')
brrez1.place(relx=0.5, rely=0.45, anchor='w')





win.mainloop()
