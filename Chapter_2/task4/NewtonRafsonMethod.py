import math

import numpy as np

from Chapter_2.task4.AddictionFunctions import *
from Chapter_2.task4 import Swann, GoldenFusion

x0 = [3.0, 1.0]
# x0 = [0.5, 1]


def func(x):
    return x[0]**2 + 4 * x[1]**2 + x[0] * x[1] + x[0]

# # Test Function
# def func(x):
#     return 2*x[0]**2 + x[1]**2 + x[0] * x[1]


def main():
    print("Метод Ньютона-Рафсона")
    H = [[1, 2], [1, 8]]
    args = '{x} + t * {d}'

    x = x0
    nabla = gradient(x)
    M = 20
    eps1 = 0.1
    eps2 = 0.15
    print(f'Проверка выполнения критерия окончания ||▽f(x1_{x[0]},x2_{x[1]})|| < eps1_{eps1} - ', end='')
    if norm(nabla) < eps1:
        print(f'критерий выполнен => x* = x_{x}')
        print(x)
        return
    print('не выполнен\n')

    k = 0

    H = hessian_matrix(func, x)
    print(f"Определяем матрицу Гессе: \n{H}")

    H = np.linalg.inv(H)
    print(f"Находим обратную матрицу Гессе:\n {H}")

    print("Проверяем является ли полученная матрица Гессе - положительно определенной - ", end='')
    if is_positive_definite(H):
        print("да =>")
        d = -matrix_vector_multiply(H, gradient(x))
        print(f"=> Определяем величину: d{k} = -1 * H(x{k}_{x}) * ▽f(x{k}_{x}) = {d} =>")
        temp_args = (args.format(x=x[0], d=d[0]), args.format(x=x[1], d=d[1]))
    else:
        print("нет => ")
        d = -gradient(x)
        print(f"=> Определяем величину: d{k} = -1 * ▽f(x{k}_{x}) = {d} =>")
        temp_args = (args.format(x=x[0], d=d[0]), args.format(x=x[1], d=d[1]))

    print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} + t{k} * d{k}) -> min')

    print()
    segment = Swann.run(func, temp_args)
    print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

    print(f'Методом золотого сечения определили величину t{k}:')
    t = GoldenFusion.run(func, temp_args, segment)

    nx = list(eval(arg.replace('t', str(t))) for arg in temp_args)
    print(f'x{k + 1} = x{k} + t{k} * d{k} = {nx}\n')

    fx, fnx = func(x), func(nx)

    double_check = 0

    k = 1
    print(f'Проверка выполнения условий:\n k_{k} < M_{M}, ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')
    while k < M and (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(fnx - fx) > eps2 or double_check < 1):

        if not (norm(tuple(nx[i] - x[i] for i in range(2))) > eps2 or abs(fnx - fx) > eps2):
            print('------------------------------------------------------------------------------------------------------------------------')
            print(f'Выполняются условия: ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} < eps2_{eps2} и |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} < eps2_{eps2} =>')
            print('=> делаем дополнительную итерацию для проверки на зацикливание')
            print('------------------------------------------------------------------------------------------------------------------------')
            double_check += 1
        elif double_check != 0:
            double_check = 0

        print(f'Итерация k = {k}')

        nabla = gradient(nx)
        print(f'Проверка выполнения критерия окончания: ||▽f(x1_{x[0]},x2_{x[1]})||={norm(nabla)} < eps1_{eps1} - ',
              end='')
        if norm(nabla) < eps1:
            print(f'критерий выполнен =>')
            print(f'=> x* = x_{x} => градиент ~ равен нулю')
            return
        print()

        H = hessian_matrix(func, x)
        print(f"Определяем матрицу Гессе: {H}")

        H = np.linalg.inv(H)
        print(f"Находим обратную матрицу Гессе: {H}")

        print("Проверяем является ли полученная матрица Гессе - положительно определенной - ", end='')
        if is_positive_definite(H):
            print("да =>")
            d = -matrix_vector_multiply(H, gradient(x))
            print(f"=> Определяем величину: d{k} = -1 * ▽f(x{k}) = {d} =>")
            temp_args = (args.format(x=nx[0], d=d[0]), args.format(x=nx[1], d=d[1]))
        else:
            d = -gradient(x)
            temp_args = (args.format(x=nx[0], d=d[0]), args.format(x=nx[1], d=d[1]))

        print(f'Определяем величину t{k} из улсловия: f(x{k}_{(x[0], x[1])} + t{k} * d{k}) -> min')

        segment = Swann.run(func, temp_args)
        print(f'Методом Свенна определили начальный интервал неопределенности: [a{k}, b{k}] = [{segment[0]}, {segment[1]}]')

        print(f'Методом золотого сечения определили величину t{k}:')
        t = GoldenFusion.run(func, temp_args, segment)

        x, fx = nx, fnx

        nx = list(eval(arg.replace('t', str(t))) for arg in temp_args)
        fnx = func(nx)
        print(f'x{k + 1} = x{k} + t{k} * d{k} = {nx}\n')
        k += 1

        print(f'Проверка выполнения условий:\nk_{k} < M_{M}, ||x{k + 1} - x{k}||={norm(tuple(nx[i] - x[i] for i in range(2)))} > eps2_{eps2}, |f(x{k + 1} - f(x{k})|={abs(func(nx) - func(x))} > eps2_{eps2}')

    print()
    if k >= M:
        print('Предельное число итераций достигнуто')
    else:
        print(f'Необходимые условия достигнуты => x = {nx}, f(x) = {func(nx)}')


if __name__ == '__main__':
    main()