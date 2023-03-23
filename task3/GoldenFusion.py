def func(x):
    return x**2 + 2


def main():
    print('Метод Золотого сечения\n')

    a, b = (-3, 7)
    k = 0
    eps = 0.000005
    gold = (3 - 5**0.5) / 3
    y = a + gold * (b - a)
    z = a + b - y

    while abs(b - a) > 2 * eps:

        leftF = func(y)
        rightF = func(z)
        print(f'Сравним f(y_{k}) & f(z_{k})')

        if leftF <= rightF:
            print(f'( f(y_{k}) <= f(z_{k}) )\n')
            b = z = y = a + b - y

        else:
            print(f'( f(y_{k}) > f(z_{k}) )\n')
            a = y = z = a + b - z

        y = a + gold * (b - a)
        z = a + b - y
        k += 1

    print(f'x* = {(a + b) / 2} +(-) {(b-a)/2}')


if __name__ == '__main__':
    main()