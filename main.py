import tkinter as tk
from tkinter import filedialog as fd
import numpy as np
from PIL import Image



def callback():
    name= fd.askopenfilename() 
    print(name)
def shifr():
    str = entry1.get()
    img = Image.open(str)
    arr = np.array(img, dtype='uint8')
    print(arr)
    print(str)
def deshifr():
    return 0
errmsg = 'Error!'
tk.Button(text='Выбрать файл',
       command=callback).pack(fill=tk.X)
tk.Button(text='выбрать файл',
       command=callback).pack(fill=tk.X)
tk.Button(text='Зашифровать',
       command=callback).pack(fill=tk.X)
tk.Button(text='Расшифровать',
       command=callback).pack(fill=tk.X)
entry1=tk.Text()

tk.mainloop()