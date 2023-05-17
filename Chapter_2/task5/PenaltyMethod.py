from Chapter_2.task5 import FletcherRivesMethod
from Chapter_2.task5 import FastersGradDown


x0 = [3, 1]
# x0 = [-1, 3]
# x0 = [-0.5, 0]

func = None


def func1(x):
    return x[0]**2 + 4 * x[1]**2 + x[0] * x[1] + x[0]


def func2(x):
    return 7 * x[0]**2 + 2 * x[1]**2 - x[0] * x[1] + x[0]


def Testfunc(x):
    return x[0]**2 + x[1]**2


def gFunc(x):
    return x[0] + x[1] - 2


def Fkfunc(x):
    # global P
    # print(P, (r / 2) * gFunc(x)**2)
    return func(x) + (r / 2) * gFunc(x)**2


def main():
    print(f'Метод штрафов')
    global r

    global func
    func = func1

    x = x0
    r = 1
    C = 1.5
    eps = 0.15

    k = 0

    print(f'''Начальные данные:
        x{k} = {tuple(x0)}, r{k} = {r}, C = {C}, eps = {eps}\n''')

    print(f'Итерация k = {k} ')
    print(f'Составим вспомогательную функцию: F(x_{x}, r{k}) = f(x_{x}) + (r{k} / 2) * g(x_{x})^2')
    x = FletcherRivesMethod.run(Fkfunc, x)
    print(f'Найдем точку x*(r{k}) - безусловного минимума функции F(x_{x}, r{k})')
    print(f'Используя метод Флетчера-Ривса: x*(r{k}) = {x}')

    P = (r / 2) * gFunc(x)**2
    print(f'Вычислим значение штрафной функции: P(x*(r{k}), r{k}) = (r{k} / 2) * g(x_{x})^2 = {P}')

    print(f'Проверка выполения условия: P_{P} <= eps_{eps} - ', end='')
    while P > eps:
        print('не выполняется => ')
        r = r * C
        print(f'=> r{k+1} = C * r{k} = {r}, x{k+1} = x*(r{k}) = {x}, k = k + 1\n')
        k += 1
        print(f'Итерация k = {k}')
        print(f'Составим вспомогательную функцию: F(x_{x}, r{k}) = f(x_{x}) + (r{k} / 2) * g(x_{x})^2')
        x = FletcherRivesMethod.run(Fkfunc, x)
        print(f'Найдем точку x*(r{k}) - безусловного минимума функции F(x_{x}, r{k})')
        print(f'Используя метод Флетчера-Ривса: x*(r{k}) = {x}')

        P = (r / 2) * gFunc(x)**2
        print(f'Вычислим значение штрафной функции: P(x*(r{k}), r{k}) = (r{k} / 2) * g(x_{x})^2 = {P}')
        print(f'Проверка выполения условия: P_{P} <= eps_{eps} - ', end='')

    print('выполняется => ')
    print(f'x* = x*(r{k}) = {x}, f(x*) = {func(x)}')


if __name__ == '__main__':
    main()