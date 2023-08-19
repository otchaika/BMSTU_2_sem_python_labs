import math as m
ORBIT = 20
def rotate_lop(x, y, xo, yo, angle):
    x = ORBIT * m.cos((angle % 360) * (m.pi / 180)) + xo
    y = ORBIT * m.sin((angle % 360) * (m.pi / 180)) + yo
    return x, y