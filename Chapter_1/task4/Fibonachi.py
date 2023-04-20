def func(x):
    return 2 * x**2 - 12 * x


def get_min_fibo(min_fib):
    last_fib, fib = (1, 1)
    n = 1
    while fib < min_fib:
        last_fib, fib = fib, last_fib + fib
        n += 1
    return (n, last_fib, fib)


def main():
    print('Метод Фибоначи\n')
    a, b = (0, 10)
    L = abs(b - a)
    l = 1
    eps = 0.1**2

    n, last_fib, fib = get_min_fibo(L / l)
    z = a + (last_fib / fib) * (b - a)
    y = a + b - z

    k = 0
    while k != n - 2:
        fy, fz = (func(y), func(z))
        print(f'Сравниваем f(y_{y}) и f(z_{z})')
        if fy <= fz:
            print(f'f(y_{y}) <= f(z_{z})\n')
            b, z = (z, y)
            y = a + b - z
        else:
            print(f'f(y_{y}) > f(z_{z})\n')
            a, y = (y, z)
            z = a + b - y
        k += 1

    y = (a + b) / 2
    z = y + eps
    fy, fz = (func(y), func(z))

    if fy <= fz:
        b = z
    else:
        a = y

    print(f'x* ∈ [{a}, {b}]\nx* = {(a + b) / 2} +(-) {(b - a) / 2}')


if __name__ == '__main__':
    main()