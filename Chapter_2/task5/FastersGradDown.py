import math

import numpy as np

from Chapter_2.task5 import Swann, GoldenFusion

func = None
x0 = None
# x0 = (0.5, 1)


# def func(x):
#     return x[0]**2 + 4 * x[1]**2 + x[0] * x[1] + x[0]


# # Test Function
# def func(x):
#     return 2*x[0]**2 + x[1]**2 + x[0] * x[1]


# # Test Grad
# def grad(x):
#     return 4*x[0] + x[1], x[0] + 2*x[1]
#

def grad(xk):
    x = np.array(xk, dtype=float)
    h = 1e-6
    grad = np.zeros_like(x)

    for i in range(len(x)):
        xi = x.copy()
        xi[i] += h
        df = func(xi) - func(x)
        grad[i] = df / h

    return list(grad)


def run(temp_func, temp_x0):
    global func
    func = temp_func

    global x0
    x0 = temp_x0
    # print('Метод наискорейшего градиентного спуска')
    arg = '{x} - t * {gx}'

    x = x0
    nabla = grad(x)

    M = 20
    eps1 = 0.1
    eps2 = 0.15
    # print(f'Проверка выполнения критерия окончания ||▽f(x1_{x[0]},x2_{x[1]})|| < eps1_{eps1} - ', end='')
    if norm(nabla) < eps1:
        # print(f'критерий выполнен => x* = x_{x}')
        # print(x)
        return x
    # print('не выполнен\n')

    k = 0
    # print(f'Итерация k = {k}')

    temp_args = (arg.format(x=x[0], gx=nabla[0]), arg.format(x=x[1], gx=nabla[1]))
    # print(temp_args)

    # print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} - t{k} * ▽f(x{k})_{(nabla[0], nabla[1])}) -> min')

    segment = Swann.run(func, temp_args)
    # print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

    # print(f'Методом золотого сечения определили величину t{k}:')
    t = GoldenFusion.run(func, temp_args, segment)
    # print(t)

    nx = tuple(eval(arg.replace('t', str(t))) for arg in temp_args)
    # print(f'x{k+1} = x{k} - t{k} * ▽f(x{k}) = {nx}\n')

    fx, fnx = func(x), func(nx)

    double_check = 0

    # print(f'Проверка выполнения условий:\n k_{k} < M_{M}, ||x{k+1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k+1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')
    while k < M and (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(func(nx) - func(x)) > eps2 or double_check < 1):

        if not (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(func(nx) - func(x)) > eps2):
            # print('------------------------------------------------------------------------------------------------------------------------')
            # print(f'Выполняются условия: ||x{k+1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} < eps2_{eps2} и |f(x{k+1} - f(x{k})|={abs(func(nx) - func(x))} < eps2_{eps2} =>')
            # print('=> делаем дополнительную итерацию для проверки на зацикливание')
            # print('------------------------------------------------------------------------------------------------------------------------')
            double_check += 1
        elif double_check != 0:
            double_check = 0

        k += 1
        x, fx = nx, fnx

        # print(f'Итерация k = {k}')

        nabla = grad(nx)
        # print(f'Проверка выполнения критерия окончания: ||▽f(x1_{x[0]},x2_{x[1]})||={norm(nabla)} < eps1_{eps1} - ', end='')
        if norm(nabla) < eps1:
            # print(f'критерий выполнен => x* = x_{x} =>')
            # print(f'Градиент ~ равен нулю')
            return x
        # print()

        # print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} - t{k} * ▽f(x{k})_{(nabla[0], nabla[1])}) -> min')
        temp_args = (arg.format(x=x[0], gx=nabla[0]), arg.format(x=x[1], gx=nabla[1]))

        segment = Swann.run(func, temp_args)
        # print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

        # print(f'Методом золотого сечения определили величину t{k}: ', end='')
        t = GoldenFusion.run(func, temp_args, segment)

        # print(f'x{k + 1} = x{k} - t{k} * ▽f(x{k}) = {nx}\n')
        nx = tuple(eval(arg.replace('t', str(t))) for arg in temp_args)
        fnx = func(nx)
        # print(f'Проверка выполнения условий:\nk_{k} < M_{M}, ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')

    # print()
    if k >= M:
        print('Предельное число итераций достигнуто')
    # else:
    #     print(f'Необходимые условия достигнуты => x = {nx}, f(x) = {func(nx)}')
        # print(nx)
        # print(func(nx))

    return nx


def norm(x):
    return math.sqrt(sum(i * i for i in x))