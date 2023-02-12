# В этом модуле происходит подсчет заданного выражения из entry.
def check_calc(string):
    # эта функция проверяет корректность введенного выражения. В случае некорректного ввода возвращает 'WRONG'
    chars = ['1', '0', '-', '+', '*', '.']
    symbols = ['-', '+', '*', '.']
    for i in range(len(string) - 1):
        if string[i] not in chars:
            return 'WRONG'
        if string[i] and string[i + 1] in symbols:
            return 'WRONG'


def to_10(a):
    # функция переводит вещественное число из двоичной в десятиричную сс. Возвращает переведенное число в формате float
    negative = False
    try:
        a = float(a)
    except:
        print('not float')
        return 'error'
    a = str(a)
    for i in range(len(a)):
        if a[i] != '0' and a[i] != '1' and a[i] != '.' and a[i] != '-':
            print('not 1 0 . -', a[i], a)
            return 'error'
    point = a.index('.')
    # происходит разделение числа на целую и дробную часть. каждая считается отдельно
    if a[0] == '-':
        start = full_to_10(a[1:point])
        negative = True
    else:
        start = full_to_10(a[:point])
    end = str(part_to_10(a[point + 1:]))[1:]
    res = ''
    if negative:
        res = '-'
    res += str(start)
    res += str(end)
    return res


def to_2(a):
    # функция переводит число из десятиричной в двоичную сс
    negative = False
    a = str(a)
    point = a.index('.')
    if a[0] == '-':
        start = full_to_2(a[1:point])
        negative = True
    else:
        start = full_to_2(a[:point])
    end = str(part_to_2(a[point + 1:]))[1:]
    res = ''
    if negative:
        res = '-'
    res += str(start) + '.'
    res += str(end)
    return res


# далее функции part и full считают дробные и целые части и выводят результат, который складывается в основных функциях
def full_to_2(a):
    length = len(a)
    res = ''
    a = int(a)
    if a == 0:
        res = '0'
    while a != 0:
        res += str(a % 2)
        a = a // 2
    return res[::-1]


def part_to_2(a):
    length = len(a)
    a = float(a)
    if a == 0:
        res = '0'
    else:
        res = ''
        while a > 1:
            a = a / 10
        for i in range(7):
            a *= 2
            if a >= 1:
                res += '1'
                a -= 1
            else:
                res += '0'
        while res[-1] == '0':
            res = res[:-1]
    return res


def full_to_10(a):
    length = len(a)
    res = 0
    for i in range(len(a)):
        res = res + int(a[i]) * 2 ** (length - i - 1)
    return res


def part_to_10(a):
    res = 0
    for i in range(len(a)):
        res = res + int(a[i]) * 2 ** (-i - 1)
    return res
    pass


def split_to_calcs(a):
    # эта функция разделяет введенную строку на числа и операторы (к примеру, '11.1-10' -> ['11.1', '-', '10']).
    # Выводит массив arr
    numb = ''
    calcs = []
    for i in range(len(a)):
        numb += a[i]
        if (a[i] == '-' and i != 0) or a[i] == '+' or a[i] == '*':
            numb = numb[:-1]
            try:
                c = float(numb)
            except:
                return 'WRONG'
            real_numb = to_10(numb)
            numb = ''
            calcs.append(float(real_numb))

            calcs.append(a[i])
    try:

        c = float(numb)
    except:
        return 'WRONG'
    real_numb = to_10(numb)
    numb = ''

    calcs.append(float(real_numb))
    print('was split')
    return calcs


def calculate_string(string):
    if '\n' in string:
        string = string[:-1]
    chars = ['1', '0', '-', '+', '*', '.']
    for j in range(len(string)):
        if string[j] not in chars:
            return 'ERROR'
    # проверка выражения на правильность
    arr = split_to_calcs(string)
    if arr == 'WRONG':
        return 'ERROR'
    new = ''
    for i in range(len(arr)):
        new += str(arr[i])
    new_str = to_2(eval(new))
    return new_str

