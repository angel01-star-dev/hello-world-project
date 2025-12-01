import tkinter as tk
from tkinter import * # импортируем все из tk

root = tk.Tk() #можно зажать ctrl и увидеть что находится в tk

root.title("я тупой программист")
root.iconbitmap(default="C:/Users/User/Downloads/element-3_99623.ico")
root.geometry("300x300")

label_1_first_str = Label(text = "я хочу спать и купить красный бархат")
label_1_first_str.pack()

root.mainloop()