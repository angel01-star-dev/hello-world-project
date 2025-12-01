# hello-world-project

Чекмарева Виктория
```py
print("Hello world")
```


## мое первое консольное окно
```py
import tkinter as tk
from tkinter import * # импортируем все из tk

root = tk.Tk() #можно зажать ctrl и увидеть что находится в tk

root.title("я тупой программист")
root.iconbitmap(default="C:/Users/User/Downloads/element-3_99623.ico")
root.geometry("300x300")

label_1_first_str = Label(text = "я хочу спать и купить красный бархат")
label_1_first_str.pack()

root.mainloop()
```

### Визуал приложения
![картинка](https://github.com/angel01-star-dev/hello-world-project/blob/main/pics2/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-12-01%20104409.png?raw=true)

## Для Linux:
```bash
python3 main.py
```

## Для Windows:
```bash
python main.py
```

## задача из ЕГЭ
```py
s = '1' + '8' * 80
#print(s)
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    if '288' in s:
        s = s.replace('288', '3', 1)
    if '3888' in s:
        s = s.replace('3888', '1', 1)
print(s)
```
или если хотите видеть все вычислительные процессы
```py
s = '1' + '8' * 80
#print(s)
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    if '288' in s:
        s = s.replace('288', '3', 1)
    if '3888' in s:
        s = s.replace('3888', '1', 1)
    print(s)
```
