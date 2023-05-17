def run(func, args, segment):
    # print('Метод Золотого сечения\n')

    a, b = segment
    k = 0
    eps = 0.1**4
    gold = (3 - 5**0.5) / 3
    y = a + gold * (b - a)
    z = a + b - y

    while abs(b - a) > 2 * eps:

        leftF = func(tuple(eval(arg.replace('t', str(y))) for arg in args))
        rightF = func(tuple(eval(arg.replace('t', str(z))) for arg in args))
        # print(f'Сравним f(y_{k}) & f(z_{k})')

        if leftF <= rightF:
            # print(f'( f(y_{k}) <= f(z_{k}) )\n')
            b = z = y = a + b - y

        else:
            # print(f'( f(y_{k}) > f(z_{k}) )\n')
            a = y = z = a + b - z

        y = a + gold * (b - a)
        z = a + b - y
        k += 1

    # print(f't* = {(a + b) / 2} +(-) {(b - a) / 2}')
    return (a + b) / 2
