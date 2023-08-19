import math as m

def find_the_dots(arr):
    minsq = -1
    rad = 0
    dots = []
    c = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                x1, y1 = arr[i][0], arr[i][1]
                x2, y2 = arr[j][0], arr[j][1]
                x3, y3 = arr[k][0], arr[k][1]
                # проверка точек на то, лежат ли они на одной прямой
                if (y1 == y2 and y2 == y3) or (x2 == x1 and x2 == x3):
                    break
                if not (y2 == y1 and y2 != y3) and not (x2 == x1 and x2 != x3):
                    if (y3 == y2 and y2 == y1) or (x3 == x2 and x2 == x1) or (
                            (x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1)):
                        break
                # нахождение центра окружности
                x0 = -0.5 * (y1 * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2) + y2 * (
                            x3 ** 2 + y3 ** 2 - x1 ** 2 - y1 ** 2) +
                             y3 * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2))

                x11 = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                if x11 == 0:
                    break
                y0 = 0.5 * (x1 * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2) + x2 * (
                            x3 ** 2 + y3 ** 2 - x1 ** 2 - y1 ** 2) +
                            x3 * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2))
                y11 = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                if y11 == 0:
                    break
                x0 = x0 / x11
                y0 = y0 / y11
                r = m.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
                # нахождение площадей круга и треугольника
                kr_sq = m.pi * (r ** 2)
                tr_sq = 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
                sq = abs(kr_sq - tr_sq)
                if minsq == -1 or sq < minsq:
                    minsq = sq
                    dots = [arr[i], arr[j], arr[k]]
                    rad = r
                    c = [x0, y0]
                    print(dots)

    return dots, rad, c
