from math import *
import tkinter as tk
import numpy as np

# функция
def f(x):
	return eval(entry_f.get())

# уточнение корней
def secant_method(a, b, eps):
	if (abs(f(a)) < eps):
		return (a, f(a))
	if (abs(f(b)) < eps):
		return (b, f(b))

	while not ((b - a) < eps):
		c = (a + b) / 2
		if (f(b) * f(c)) < 0:
			a = c
		else:
			b = c
	return ((b + a) / 2, f((b + a) / 2))


# запуск
def start():
	a = float(entry_a.get())
	b = float(entry_b.get())
	eps = float(entry_eps.get())

	array = secant_method(a, b, eps)
	print("x: {:<9.4}\nf(x): {:<.0e}".format(array[0], array[1]))

# Создание окна
win = tk.Tk()

# заголовок
win.title('Lab_2_2_def')

# создание надписи ВВОД
lb_f = tk.Label(win, text='f(x):')
lb_f.grid(row=0, column=0)

# Создание поля ввода
entry_f = tk.Entry(win)
entry_f.grid(row=1, column=0)

# создание надписи ВВОД
lb_a = tk.Label(win, text='a:')
lb_a.grid(row=0, column=1)

# Создание поля ввода
entry_a = tk.Entry(win)
entry_a.grid(row=1, column=1)

# создание надписи ВВОД
lb_b = tk.Label(win, text='b:')
lb_b.grid(row=0, column=2)

# Создание поля ввода
entry_b = tk.Entry(win)
entry_b.grid(row=1, column=2)

# создание надписи ВВОД
lb_eps = tk.Label(win, text='eps:')
lb_eps.grid(row=0, column=3)

# Создание поля ввода
entry_eps = tk.Entry(win)
entry_eps.grid(row=1, column=3)


# кнопка
enter_button = tk.Button(text='start', command=start)
enter_button.grid(row=2, column=0, columnspan=6, stick='we')


# запуск обработчика обытий
win.mainloop()