import math

import Fibonachi
import Swann
from Parameters import Parameters


# def func(x):
#     x = x.get_parameters()
#     return x[0]**2 + 4 * x[1]**2 + x[0] * x[1] + x[0]

def func(x):
    x = x.get_parameters()
    return 2 * x[0]**2 + x[1]**2 + x[0] * x[1]


# def grad(x):
#     x = tuple(x.get_parameters())
#     return 2 * x[0] + x[1] + 1, 8 * x[1] + x[0]

def grad(x):
    x = tuple(x.get_parameters())
    return 4 * x[0] + x[1], x[0] + 2 * x[1]


def norm(x):
    if isinstance(x, Parameters):
        x = tuple(x.get_parameters())
    return math.sqrt(sum(i*i for i in x))


def main():
    x0 = (0.5, 1)
    x = Parameters(x0)

    M = 100
    eps = 0.1**2
    if norm(grad(x)) < eps:
        print(x)
        return

    k = 0
    segment = Swann.run(func, x)
    nx = Fibonachi.run(func, segment)
    fx, fnx = func(x), func(nx)
    while k < M and norm(nx - x) > eps and abs(fx - fnx) > eps:
        if norm(grad(nx)) < eps:
            break
        x, fx = nx, fnx
        segment = Swann.run(func, x)
        nx = Fibonachi.run(func, segment)
        fnx = func(nx)
        k += 1

    print(k)
    print(nx)


if __name__ == '__main__':
    main()