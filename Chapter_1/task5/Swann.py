def func(x):
    return (x - 5) ** 2
    # return x**2 + 2


def main():
    print('Метод Свенна')
    x = 1
    t = 1
    k = 0

    lf, f, rf = (func(x - t), func(x), func(x + t))

    if lf >= f <= rf:
        print('Проверяем условие окончания:')
        print(f'f(x_{x} - t_{t}) >= f(x_{x}) <= f(x_{x} + t_{t})')
        print(f'[a0, b0] = [{x - t}, {x + t}]')
    elif lf < f > rf:
        print('Проверяем условие окончания:')
        print(f'f(x_{x} - t_{t}) < f(x_{x}) > f(x_{x} + t_{t})')
        print('Тpебуемый интеpвал неопpеделенности не может быть найден, т.к. функция не является унимодальной')
    else:
        print('Условие окончания не выполняется\n')
        delta = None
        a, b = None, None
        nx = None

        print('Определяем величину delta')
        if lf >= f >= rf:
            print(f'f(x_{x} - t_{t}) >= f(x_{x}) >= f(x_{x} + t_{t}) => delta = {t}\n')
            delta = t
            a, nx = (x, x + t)
        else:
            print(f'f(x_{x} - t_{t}) < f(x_{x}) < f(x_{x} + t_{t}) => delta = {-t}\n')
            delta = -t
            b, nx = (x, x - t)
        k = 1

        x = nx
        nx = x + 2 ** k * delta
        print('Проверка условия убывания функции')
        while func(nx) < func(x):
            if delta == t:
                print(f'f(nx_{nx}) < f(x_{x}) и delta = {t} => a = {x**k}\n')
                a = x**k
            else:
                print(f'f(nx_{nx}) < f(x_{x}) и delta = {-t} => b = {x**k}\n')
                b = x**k

            k += 1
            x = nx
            nx = x + 2**k * delta

        if delta == t:
            print(f'f(nx_{nx}) >= f(x_{x}) и delta = {t} => b = {nx}\n')
            b = nx
        else:
            print(f'f(nx_{nx}) >= f(x_{x}) и delta = {-t} => a = {nx}\n')
            a = nx

        print(f'[a0, b0] = [{a}, {b}]')


if __name__ == '__main__':
    main()