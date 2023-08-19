from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox as box
from tkinter import filedialog as fd


def encode_char(char):
    num_int = char.encode("koi8-r")
    num_bin = bin(num_int[0])[2:]
    num_bin = (8 - len(num_bin)) * "0" + num_bin
    return num_bin


def massage_to_bin(massage):
    bin_massage = ""
    for char in massage:
        num_bin = encode_char(char)
        bin_massage += num_bin
    return bin_massage


def decode_char(num_bin):
    num_int = int(num_bin, 2)
    num_byte = num_int.to_bytes(1, byteorder="big")
    char = num_byte.decode("koi8-r")
    return char


def encode_message_1(width, height, pix, bin_message, draw):
    index = 0

    for x in range(width):
        for y in range(1, height):
            for z in range(3):

                if index == len(bin_message):
                    return pix

                bit = int(bin_message[index])
                channel = pix[x, y][z]

                if (bit == 0b0):
                    channel &= ~0b1
                else:
                    channel |= 0b1

                channels = list(pix[x, y])
                channels[z] = channel
                channels = tuple(channels)

                draw.point((x, y), channels)
                index += 1


def encode_message_2(width, height, pix, bin_message, draw):
    index = 0
    lenn=len(bin_message)
    lenn = (24-len(bin(lenn)))*'0'+bin(lenn)
    lenn_t=(int(lenn[0:8],2), (lenn[8:16],2), int(lenn[16:24],2))
    draw.point((0,0),lenn_t)
    print(pix[0][0], 'THIS PIX')
    channels=[]
    for x in range(width):
        for y in range(1, height):
            for z in range(3):
                if index == len(bin_message):
                    return pix

                bit = int(bin_message[index])
                channel = pix[x][y][z]
                channel=bin(channel)
                #channel = (8-len(channel))*'0'+channel
                print(bin_message[index:index+1])
                channel=channel[:-1]+bin_message[index:index+1]
                channel=int(channel, 2)
                draw.point((x, y), z)
                print(channel, x, y, z)
                #channel = pix[x, y][z]
                if z!=0:
                    channels = list(pix[x][y])
                    channels[z] = channel
                if z==2:
                    channels = list(pix[x][y])
                    channels[z] = channel
                    channels = tuple(channels)

                    draw.point((x, y), channels)
                    print(channels)
                pix[x][y][z]=channel
                #im = Image.fromarray(pix, mode='RGB')
                index += 1



                """if (bit == 0b0):
                    channel &= ~0b1
                else:
                    channel |= 0b1"""
"""
                channels = list(pix[x, y])
                channels[z] = channel
                channels = tuple(channels)

                draw.point((x, y), channels)"""


def decode_image_1(width, height, pix):
    string = ""
    byte = ""
    count_channels = len(pix[0, 0])
    count_bits = 0
    len_message = pix[0, 0][0]
    index = 0
    for x in range(width):
        for y in range(1, height):
            for z in range(3):
                channel = pix[x, y][z]
                if (count_bits == 4):
                    print(byte, x, y, z)
                    char = decode_char(byte)
                    if (char == "@"):
                        return string

                    string += char
                    count_bits = 0
                    byte = ""
                channel = pix[x, y][z]
                channel=bin(channel)
                byte=channel[:-1]
                print(channel, 'channel')
                bit = channel & 0b1
                count_bits += 1
                index += 1
def decode_image(width, height, pix):
    string = ""
    byte = ""
    len_message=pix[0,0]
    count_bits = 0
    index = 0
    for x in range(width):
        for y in range(1, height):
            for z in range(3):
                channel = bin(pix[x, y][z])
                bit=channel[-1]
                if (count_bits == 8):
                    print(byte, x, y, z)
                    char = decode_char(byte)
                    string += char
                    count_bits = 0
                    byte = ""

                    #if (char == "@"):
                        #return string
                    if index==len_message:
                        return string
                byte+=bit
                channel = pix[x, y][z]
                print(channel, 'channel')
                #bit = channel & 0b1
                byte += str(channel)
                count_bits += 1
                index += 1


def info():
    box.showinfo('Описание программы',
                 "Программа шифрует сообщения в выбранный файл png и расшифровывает их")


def choose_file_in():
    filetypes = (('image files', '*.PNG'),)
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    image = Image.open(filename)
    chosen_file_in.delete(1.0, 'end')
    chosen_file_in.insert('1.0', filename)


def encode_massage():
    filetypes = (('image files', '*.PNG'),)
    filename = chosen_file_in.get(1.0, 'end')[:-1]
    if filename[-4:] != ".png":
        box.showinfo("Ошибка.", "Картинка не выбрана, либо не соответствует формату. "
                                "Выберете .png картику для расшифровки")
        return 0
    name = filename.split("/")[-1]
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    print(pix[0, 0])
    massage = entry_input.get(1.0, 'end')
    end_point = "@"
    massage = massage + end_point
    bin_massage = massage_to_bin(massage)
    im = encode_message_2(width, height, pix, bin_massage, draw)

    box.showinfo("Успех", "Сообщение успешно зашифровано, выберете путь для сохранения зашифрованной картики")

    folder = fd.askdirectory()
    full_name = folder + '/encoded_' + name
    image.save(full_name, 'PNG')
    chosen_file_out.delete(1.0, 'end')
    chosen_file_out.insert(1.0, full_name)
    print(folder + name)
    box.showinfo("Успех", "Картинка успешно сохранилась")


def choose_file_out():
    filetypes = (('image files', '*.PNG'),)
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    image = Image.open(filename)
    chosen_file_out.delete(1.0, 'end')
    chosen_file_out.insert('1.0', filename)


def decode_massage():
    filetypes = (('image files', '*.PNG'),)
    filename = chosen_file_out.get(1.0, 'end')[:-1]
    if filename[-4:] != ".png":
        box.showinfo("Отчёт", "Картинка не выбрана, либо не соответствует формату. "
                              "Выберете .png картику для расшифровки")
    name = filename.split("/")[-1]
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    string = decode_image(width, height, pix)
    box.showinfo("Успешно", "Сообщение успешно расшифровано")
    decoded_message.delete(1.0, 'end')
    decoded_message.insert(1.0, string)


def block_insertion_in(event):
    return "break"


def block_insertion_out(event):
    return "break"


# Создание окна
# --------------------------------------------------------------------------
win = tk.Tk()
win.resizable(width=False, height=False)
win.title('Lab_3_2')
# --------------------------------------------------------------------------


# Основное меню
# --------------------------------------------------------------------------
mmenu = tk.Menu(win)
win.config(menu=mmenu)
pmenu = tk.Menu(mmenu)
pmenu.add_command(label='Информация', command=info)
mmenu.add_cascade(label='Меню', menu=pmenu)
win.columnconfigure(0, minsize=100, weight=0)
win.columnconfigure(1, minsize=100, weight=0)
win.rowconfigure(0, minsize=100, weight=0)
win.rowconfigure(1, minsize=100, weight=0)
win.rowconfigure(2, minsize=100, weight=0)
win.rowconfigure(3, minsize=100, weight=0)
win.rowconfigure(4, minsize=100, weight=0)
win.rowconfigure(5, minsize=100, weight=0)
# --------------------------------------------------------------------------


# Интерфейс
# --------------------------------------------------------------------------
n = 2
a = 15
label_input = tk.Label(win, text='Сообщение, которое необходимо зашифровать:', height=n)
label_input.grid(row=0, column=0, padx=a, pady=a, sticky='wens')

entry_input = tk.Text(win, height=n, bg='yellow')
entry_input.grid(row=1, column=0, padx=a, pady=a, sticky='wens')
choose_file_in_bt = tk.Button(win, text='Выбрать файл', command=choose_file_in, height=n)
choose_file_in_bt.grid(row=2, column=0, padx=2 * a, pady=2 * a, sticky='wens')
chosen_file_in = tk.Text(win, height=n, bg='yellow')
chosen_file_in.grid(row=3, column=0, padx=a, pady=a, sticky='wens')
chosen_file_in.bind('<Key>', block_insertion_in)
"""entry_input_name = tk.Entry(win)
entry_input_name.grid(row=3, column=0, padx=5, pady=5)"""
encode_button = tk.Button(win, text="Зашифровать сообщение", command=encode_massage, height=n)
encode_button.grid(row=4, column=0, stick='wens', padx=a, pady=a, sticky='wens')

# Decoding--------------------------------------------------------------------
label_input = tk.Label(win, text='Декодирование', height=n)
label_input.grid(row=0, column=1, padx=a, pady=a, sticky='wens')

choose_file_out_bt = tk.Button(win, text='Выбрать файл', command=choose_file_out, height=n)
choose_file_out_bt.grid(row=1, column=1, padx=2 * a, pady=2 * a, sticky='wens')
chosen_file_out = tk.Text(win, height=n, bg='yellow')
chosen_file_out.grid(row=2, column=1, padx=a, pady=a, sticky='wens')
chosen_file_out.bind('<Key>', block_insertion_out)

decode_button = tk.Button(win, text="Расшифровать сообщение", command=decode_massage, background='green')
decode_button.grid(row=3, column=1, stick='wens', padx=2 * a, pady=2 * a, sticky='wens')

label_output = tk.Label(win, text='Вывод сообщения:', height=n)
label_output.grid(row=4, column=1, padx=a, pady=a, sticky='wens')

decoded_message = tk.Text(win, height=n, bg='yellow')
decoded_message.grid(row=5, column=1, padx=a, pady=a, sticky='wens')
for c in range(1):
    win.columnconfigure(c, weight=1)
for r in range(6):
    win.rowconfigure(r, weight=1)
win.mainloop()
