def get_min_fibo(min_fib):
    # min_fib = min_fib.get_max()
    # last_fib, fib = (1, 1)
    # n = 1
    # while fib < min_fib:
    #     last_fib, fib = fib, last_fib + fib
    #     n += 1
    # return (n, last_fib, fib)

    min_fibs = min_fib.get_parameters()
    lf, f, n = [], [], 1
    for min_fib in min_fibs:
        last_fib, fib = (1, 1)
        tn = 1
        while fib < min_fib:
            last_fib, fib = fib, last_fib + fib
            tn += 1
        lf.append(last_fib)
        f.append(last_fib)
        n = max(n, tn)
    return (n, last_fib, fib)


def run(func, segment):
    # print('Метод Фибоначи\n')
    a, b = segment
    L = b - a
    l = 1
    eps = 0.1**2

    n, last_fib, fib = get_min_fibo(L / l)
    z = a + L * (last_fib / fib)
    y = a + b - z

    k = 0
    fy, fz = (func(y), func(z))
    while k != n - 2:
        # print(f'Сравниваем f(y_{y}) и f(z_{z})')
        if fy <= fz:
            # print(f'f(y_{y}) <= f(z_{z})\n')
            b, z, fz = (z, y, fy)
            y = a + b - z
            fy = func(y)
        else:
            # print(f'f(y_{y}) > f(z_{z})\n')
            a, y, fy = (y, z, fz)
            z = a + b - y
            fz = func(z)
        k += 1

    y = (a + b) / 2
    z = y + eps
    fy, fz = (func(y), func(z))

    if fy <= fz:
        b = z
    else:
        a = y

    # print(f'x* ∈ [{a}, {b}]\nx* = {(a + b) / 2} +(-) {(b - a) / 2}')
    return (a + b) / 2