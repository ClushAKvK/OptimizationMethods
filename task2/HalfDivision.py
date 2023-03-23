def func(x):
    return x**2 + 2


def main():
    print('Метод половинного деления\n')
    a, b = (-3, 7)
    L = abs(b - a)
    l = 1

    x = (a + b) / 2
    while L > l:
        y, z = (a + L/4, b - L/4)
        fx, fy, fz = (func(x), func(y), func(z))

        print(f'Сравним f(y_{y}) и f(x_{x}):')
        if fy < fx:
            print(f'f(y_{y}) < f(x_{x})\n')
            b, x = (x, y)
        elif fz < fx:
            print(f'f(y_{y}) >= f(x_{x}) & f(z_{z}) < f(x_{x})\n')
            a, x = (x, z)
        else:
            print(f'f(y_{y}) >= f(x_{x}) & f(z_{z}) >= f(x_{x})\n')
            a, b = (y, z)
        L = abs(b - a)

    print(f'x* ∈ [{a}, {b}]\nx* = {x} +(-) {L / 2}')


if __name__ == '__main__':
    main()