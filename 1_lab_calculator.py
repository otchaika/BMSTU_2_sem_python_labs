import tkinter as tk
import module1 as md
# Составить приложение, используя модуль создания оконных приложений Tkinter, реализующее индивидуальное задание.
# Интерфейс должен предоставлять ввод символов: как числовых, так и знаков операций -- и с использованием клавиатуры,
# и с помощью кнопок приложения. Также в приложении необходимо создать меню, в котором должны быть следующие пункты:
# очистка полей ввода/вывода (по одному и всех сразу),
# информация о программе и авторе.
# Использование встроенных функций bin(), oct(), hex() запрещено.
# Сложение, вычитание и умножение вещественных чисел в 2-й системе счисления.
calculation = ''

hidden = True


def autor():
    global hidden
    global autor_label
    if not hidden:
        autor_label.grid_remove()
        hidden = True
    else:
        autor_label.grid(row=6, columnspan=3)
        hidden = False


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    entry.delete(1.0, 'end')
    entry.insert(1.0, calculation)


def evaluate():
    global calculation
    calculation = entry.get(1.0, 'end')
    res = md.calculate_string(calculation)
    if res == 'ERROR':
        clear_field()
        clear_field2()
        result.insert(1.0, 'Error')
    else:
        calculation = ''
        clear_field2()
        result.insert(1.0, res)


def clear_field():
    global calculation
    calculation = ''
    entry.delete(1.0, 'end')


def clear_field2():
    global calculation
    calculation = ''
    result.delete(1.0, 'end')


def clear_fields():
    global calculation
    calculation = ''
    entry.delete(1.0, 'end')
    result.delete(1.0, 'end')


def clear_char():
    global calculation
    calculation = calculation[:-1]
    entry.delete("end-2c")


root = tk.Tk()

root['bg'] = '#008080'
root.title('Калькулятор двоичной системы')
entry = tk.Text(root, height=2)
for c in range(3): root.columnconfigure(index=c, weight=1)
for c in range(7): root.rowconfigure(index=c, weight=1)
root.minsize(height=400, width=400)
root.maxsize(height=400, width=400)


def make_button(char):
    return tk.Button(root, text=char, command=lambda: add_to_calculation(char), width=10)


entry.grid(row=0, columnspan=3, rowspan=1, sticky='ns', padx=30, pady=5)
result = tk.Text(root, height=2)
result.grid(row=1, columnspan=3, rowspan=1, sticky='ns', padx=30, pady=5)

make_button('0').grid(row=2, column=0, stick='ens', padx=5, pady=5)
make_button('1').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_button('.').grid(row=2, column=2, stick='wns', padx=5, pady=5)
make_button('*').grid(row=3, column=0, stick='ens', padx=5, pady=5)
make_button('-').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_button('+').grid(row=3, column=2, stick='wns', padx=5, pady=5)
tk.Button(root, text='clear entry', command=lambda: clear_field(), width=10).grid(row=5, column=0, sticky='ens',
                                                                                  padx=5, pady=5)
tk.Button(root, text='clear result', command=lambda: clear_field2(), width=10).grid(row=5, column=2, sticky='wns',
                                                                                    padx=5, pady=5)
tk.Button(root, text='clear all', command=lambda: clear_fields(), width=10).grid(row=4, column=0, sticky='ens',
                                                                                 padx=5, pady=5)
tk.Button(root, text='clear one', command=lambda: clear_char(), width=10).grid(row=5, column=1, sticky='wens',
                                                                               padx=5, pady=5)
tk.Button(root, text='=', command=lambda: evaluate(), width=10).grid(row=4, column=1, sticky='wens',
                                                                     padx=5, pady=5)
tk.Button(root, text='info', command=lambda: autor(), width=10).grid(row=4, column=2, sticky='wns',
                                                                     padx=5, pady=5)
autor_label = tk.Label(root, text='Siling Ekaterina IU7-25B. This calculator adds,\n '
                                  'multiplies and substracts binary numbers')
print(type(autor_label))
root.mainloop()
