import math

def move_left(i, a, x0, y0):
    angle = i * 3.14 / 180
    l = math.acos((a - 400) / math.sqrt(500 ** 2 - 400 ** 2))
    int(l)
    a = (100 * math.cos(angle + l)) + x0  # 400 - начальная точка по х и по у
    b = (100 * math.sin(angle + l)) + y0
    i += 3
    return i, a, b

def move_right(i, a, x0, y0):
    angle = i * 3.14 / 180
    l = math.acos((a - 400) / math.sqrt(500 ** 2 - 400 ** 2))
    int(l)
    a = (100 * math.cos(angle + l)) + x0
    b = (100 * math.sin(angle + l)) + y0
    i -= 3
    return i, a, b