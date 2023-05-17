import math

import numpy as np

from Chapter_2.task5 import Swann, GoldenFusion

func = None
x0 = None


def gradient(xk):
    x = np.array(xk, dtype=float)
    h = 1e-6
    grad = np.zeros_like(x)

    for i in range(len(x)):
        xi = x.copy()
        xi[i] += h
        df = func(xi) - func(x)
        grad[i] = df / h

    return list(grad)


def norm(x):
    return math.sqrt(sum(i * i for i in x))


def run(temp_func, temp_x0):
    # print('Метод Флетчера–Ривса')
    args = '{x} + t * {d}'

    global func
    func = temp_func

    global x0
    x0 = temp_x0

    x = x0
    nabla = gradient(x)

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

    last_d = [-n for n in nabla]
    # print(f'Определяем d{k}: {tuple(last_d)}' )

    temp_args = (args.format(x=x[0], d=last_d[0]), args.format(x=x[1], d=last_d[1]))
    # print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} - t{k} * ▽f(x{k})_{(nabla[0], nabla[1])}) -> min')

    segment = Swann.run(func, temp_args)
    # print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

    # print(f'Методом золотого сечения определили величину t{k}:')
    t = GoldenFusion.run(func, temp_args, segment)

    nx = tuple(eval(arg.replace('t', str(t))) for arg in temp_args)
    # print(f'x{k + 1} = x{k} - t{k} * ▽f(x{k}) = {nx}\n')

    fx, fnx = func(x), func(nx)

    double_check = 0

    last_norm_nabla = norm(nabla)

    # print(f'Проверка выполнения условий:\n k_{k} < M_{M}, ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')
    while k < M and (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(fnx - fx) > eps2 or double_check < 1):

        if not (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(fnx - fx) > eps2):
            # print('------------------------------------------------------------------------------------------------------------------------')
            # print(f'Выполняются условия: ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} < eps2_{eps2} и |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} < eps2_{eps2} =>')
            # print('=> делаем дополнительную итерацию для проверки на зацикливание')
            # print('------------------------------------------------------------------------------------------------------------------------')
            double_check += 1
        elif double_check != 0:
            double_check = 0

        k += 1
        # print(f'Итерация k = {k}')

        nabla = gradient(nx)
        # print(f'Проверка выполнения критерия окончания: ||▽f(x1_{x[0]},x2_{x[1]})||={norm(nabla)} < eps1_{eps1} - ', end='')
        if norm(nabla) < eps1:
            # print(f'критерий выполнен =>')
            # print(f'=> x* = x_{x} => градиент ~ равен нулю')
            return x
        # print()

        norm_nabla = norm(nabla)
        beta = norm_nabla**2 / last_norm_nabla**2
        # print(f'Определяем величину Beta = {beta}')

        d = [-nabla[i] + beta * last_d[i] for i in range(len(nabla))]
        # print(f'Определяем d{k} = -▽f(x{k}) + Beta * d{k - 1}: {tuple(last_d)}')

        # print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} - t{k} * ▽f(x{k})_{(nabla[0], nabla[1])}) -> min')
        temp_args = (args.format(x=nx[0], d=d[0]), args.format(x=nx[1], d=d[1]))

        segment = Swann.run(func, temp_args)
        # print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

        # print(f'Методом золотого сечения определили величину t{k}: ', end='')
        t = GoldenFusion.run(func, temp_args, segment)

        last_d, last_norm_nabla, x, fx = d, norm_nabla, nx, fnx

        # print(f'x{k + 1} = x{k} - t{k} * ▽f(x{k}) = {nx}\n')
        nx = tuple(eval(arg.replace('t', str(t))) for arg in temp_args)
        fnx = func(nx)

        # print(f'Проверка выполнения условий:\nk_{k} < M_{M}, ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')

    # print()
    if k >= M:
        print('Предельное число итераций достигнуто')
    # else:
        # print(f'Необходимые условия достигнуты => x = {nx}, f(x) = {func(nx)}')

    return nx


