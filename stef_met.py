



def find_root(iterations, x0, func_str, eps):
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
