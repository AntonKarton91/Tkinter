import tkinter as tk


class Window:
    win=tk.Tk()
    def __init__(self):
        pass
    def create_w(self):
        tk.Label(Window.win, text='HELLO').pack()

    def start(self):
        self.create_w()
        Window.win.mainloop()


win=Window()
win.start()

