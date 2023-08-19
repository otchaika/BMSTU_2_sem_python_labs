import tkinter as tk
from tkinter import messagebox as box
import module4 as m4
size=400
# по клику на поле эта функция создает точку на холсте
def click(event):
    x, y = event.x, event.y
    print(x, y)
    make_a_dot(x, y, 'grey')
    string = ' ' + str(x) + ',' + str(y) + ' '
    all_coords_text.insert('end', string)
    return 0

# удаление символа в текстовом поле
def backspace(event):
    string = all_coords_text.get(1.0, 'end')[:-1]
    all_coords_text.delete(1.0, 'end')
    all_coords_text.insert(1.0, string)

#блокирует ввод лишних символов в поле ввода
def block_insertion(event):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.']
    if event.char not in nums:
        return "break"
def block_all_insertion(event):
    return "break"

# очищает все поля
def clear_all():
    canvas.delete('all')
    all_coords_text.delete(1.0, 'end')
    chosen_dots_text.delete(1.0, 'end')

# создает точку в заданном месте
def make_a_dot(x, y, color):
    canvas.create_oval(x + 5, y + 5, x - 5, y - 5, fill=color)


# проверяет координаты на соответствие границам холста
def check(arr):
    if abs(arr[0])>size or abs(arr[1])>size:
        return 1
    """for i in range(len(arr)):
        if abs(float(arr[i][0])) > 400 or abs(float(arr[i][1])) > 400:
            return 1"""


# функция запускается при накжатии кнопки "Start"
# она обрабатывает массив точек и выводит графическое изображение результата
def start():
    canvas.delete('all')
    chosen_dots_text.delete(1.0, 'end')
    string = all_coords_text.get(1.0, 'end')[:-1]
    arr = string.split(' ')
    i = 0
    while i < len(arr):
        if arr[i] == '':
            arr.pop(i)
        else:
            if ',' not in arr[i]:
                box.showinfo('Ошибка', 'Не до конца введена координата')
                return 0
            arr[i] = arr[i].split(',')
            print(arr[i])
            if arr[i][0] == '' or arr[i][1] =='':
                box.showinfo('Ошибка', 'Неверный ввод координат.')
                return 0
            arr[i][0] = float(arr[i][0])
            arr[i][1] = float(arr[i][1])
            if len(arr[i]) != 2:
                box.showinfo('Ошибка', 'Неверный ввод координат')
                return 1
            print(arr)
            if check(arr[i]) == 1:
                box.showinfo('Ошибка', 'Соответствующих точек в поле не существует')
                return 1
            i += 1
    if len(arr) < 3:
        box.showinfo('Ошибка', 'Введите 3 или более точек')
    dots, rad, center = m4.find_the_dots(arr)
    if rad == 0:
        box.showinfo('Ошибка', 'Соответствующих точек не существует (невозможно решить задачу)')
        return
    for i in range(len(arr)):
        make_a_dot(arr[i][0], arr[i][1], 'green')
    canvas.create_line(dots[0][0], dots[0][1], dots[1][0], dots[1][1])
    canvas.create_line(dots[0][0], dots[0][1], dots[2][0], dots[2][1])
    canvas.create_line(dots[2][0], dots[2][1], dots[1][0], dots[1][1])
    canvas.create_oval(center[0] - rad, center[1] - rad, center[0] + rad, center[1] + rad)
    make_a_dot(dots[0][0], dots[0][1], 'red')
    make_a_dot(dots[1][0], dots[1][1], 'red')
    make_a_dot(dots[2][0], dots[2][1], 'red')
    d1 = dots[0]
    d2 = dots[1]
    d3 = dots[2]
    d1 = str(d1[0]) + ',' + str(d1[1]) + ' '
    d2 = str(d2[0]) + ',' + str(d2[1]) + ' '
    d3 = str(d3[0]) + ',' + str(d3[1]) + ' '
    chosen_dots_text.insert(1.0, d1 + d2 + d3)


win = tk.Tk()
win.geometry("600x600")
# Interface------------------------------------------------
interface = tk.Frame(win)
all_coords_label = tk.Label(interface, text='Введите координаты точек в виде "x1,y1 x2,y2..."')
all_coords_text = tk.Text(interface, height=2)
all_coords_text.bind('<BackSpace>', backspace)
all_coords_text.bind('<Key>', block_insertion)
chosen_dots_text = tk.Text(interface, height=1)
chosen_dots_text.bind('<Key>', block_all_insertion)
start_button = tk.Button(interface, text='Начать', command=start)
clear_button = tk.Button(interface, text='Очистить все', command=clear_all)
all_coords_label.pack()
all_coords_text.pack()
start_button.pack()
clear_button.pack()
chosen_dots_text.pack()
interface.pack()

# Canvas-------------------------------------------------
canvas = tk.Canvas(win, bg='yellow')

canvas.bind("<Button-1>", click)
canvas.config(height=size, width=size, borderwidth=2)
canvas.pack()

win.mainloop()
