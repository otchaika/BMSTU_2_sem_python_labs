# Исследуемая функция
from math import *
from tkinter.messagebox import showerror
from sympy import *
import stef_met


class CheckerException(Exception):
    pass

NO_ERRORS = True  # Корень найден без огибок
TOO_MUCH_ITERATIONS = 1  # Превышено максимальное количество итераций
INPUT_ERROR = 2
STEP_IS_TOO_BIG=3
BAD_INPUT=4
def function(func_str, x):
    func = str(simplify(func_str))
    print(func)
    a = eval(func_str)
    return float(a)

def stef_met(func_str,iterations, x0, eps):
    def f(x):
        return eval(func_str)

    def g(x):
        return f(x + f(x)) / f(x) - 1

    x = x0
    for i in range(iterations):
        x0=x
        x=x-f(x)/g(x)
        if abs(x-x0)<eps:
            return x

def half_divide_method(func_str, start_point, end_point, accuracy, max_iteration, current_iteration=0):
    mid_point = (start_point + end_point) / 2
    if current_iteration >= max_iteration:
        return ['', '', '', 2]
    if abs(function(func_str, mid_point)) < accuracy:
        return [mid_point, function(func_str, mid_point), current_iteration, False]
    elif function(func_str, mid_point) * function(func_str, start_point) < 0:
        return half_divide_method(func_str, start_point, mid_point, accuracy, max_iteration, current_iteration + 1)
    else:
        return half_divide_method(func_str, mid_point, end_point, accuracy, max_iteration, current_iteration + 1)


def find_roots(func_str, start_point, end_point, step, eps, max_iteration):
    array_of_roots = []
    x_cur = start_point
    x_next = round(x_cur + step, 10)
    if x_next > end_point:
        x_next = end_point
    while x_next <= end_point:
        if abs(function(func_str, x_cur)) < eps:
            array_of_roots.append(0)
            array_of_roots[-1] = [len(array_of_roots), '{:g}..{:g}'.format(x_cur, x_next),
                                  x_cur, function(func_str, x_cur), 1, False]
        elif function(func_str, x_cur) * function(func_str, x_next) < 0:
            array_of_roots.append(0)
            array_of_roots[-1] = ([len(array_of_roots), '{:g}..{:g}'.format(x_cur, x_next)] +
                                  half_divide_method(func_str, x_cur, x_next, eps, max_iteration))
        x_cur = x_next
        x_next = round(x_cur + step, 10)
        if x_next > end_point and end_point - x_cur > eps:
            x_next = end_point

        if abs(x_cur - end_point) < eps and abs(function(func_str, x_cur)) < eps:
            array_of_roots.append(0)
            array_of_roots[-1] = [len(array_of_roots),
                                  '{:g}..{:g}'.format(x_cur, end_point),
                                  end_point, function(func_str, end_point), 0, 0]
    return array_of_roots


# Проверка входных данных
def checker(func_str, start_point, end_point, step, eps, maxN):
    error_code = 0
    try:
        func = simplify(func_str)
    except NameError:
        return INPUT_ERROR
    try:
        res = eval(func_str)
    except NameError:
        return INPUT_ERROR
    try:
        if func_str == "" or start_point == "" or end_point == "" or \
                step == "" or eps == "" or maxN == "":
            return INPUT_ERROR
        start = float(start_point)
        end = float(end_point)
        if end <= start:
            raise CheckerException
    except CheckerException:
        error_code = 1
    if not error_code:
        try:
            step = float(step)
            if step <= 0:
                return BAD_INPUT
        except CheckerException:
            error_code = 2
    if not error_code:
        try:
            eps = float(eps)
            if eps <= 0:
                return BAD_INPUT
        except CheckerException:
            error_code = 3
    if func_str == "" or start_point == "" or end_point == "" or step == "" or eps == "" or maxN == "" and not error_code:
        error_code = 5
    if step <= eps and not error_code:
        error_code = 6
    if not error_code:
        try:
            simplify(func_str)
        except (TypeError, SyntaxError, ValueError, NameError):
            error_code = 7
    return float(start_point), float(end_point), float(step), float(eps), float(maxN), float(error_code)

print(function('1010*x**2+ln(x)', 3))
print(str(simplify('x+1')))