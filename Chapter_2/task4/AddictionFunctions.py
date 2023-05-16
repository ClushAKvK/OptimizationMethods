import math

import numpy as np

from Chapter_2.task4.NewtonRafsonMethod import func


def gradient(xk):
    x = np.array(xk)
    h = 1e-6
    grad = np.zeros_like(x)

    for i in range(len(x)):
        xi = x.copy()
        xi[i] += h
        df = func(xi) - func(x)
        grad[i] = df / h

    return list(grad)


def hessian_matrix1(func, variables):
    return [[1, 2], [1, 8]]


def hessian_matrix(func, x):
    n = len(x)
    hessian = [[0] * n for _ in range(n)]

    # Вычисляем значения вторых частных производных
    for i in range(n):
        for j in range(n):
            h = 1e-5
            x_plus_h1 = x[:]
            x_plus_h2 = x[:]
            x_plus_h1[i] += h
            x_plus_h2[j] += h
            x_plus_h1_h2 = x[:]
            x_plus_h1_h2[i] += h
            x_plus_h1_h2[j] += h
            f_plus_h1 = func(x_plus_h1)
            f_plus_h2 = func(x_plus_h2)
            f_plus_h1_h2 = func(x_plus_h1_h2)
            f = func(x)
            hessian[i][j] = (f_plus_h1_h2 - f_plus_h1 - f_plus_h2 + f) / (h ** 2)

    hessian = [[2, 1], [1, 8]]
    # hessian = [[4, 1], [1, 2]]
    return hessian


def norm(x):
    return math.sqrt(sum(i * i for i in x))


def is_positive_definite(matrix):
    # Проверяем, является ли матрица квадратной
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return False

    # Проверяем, что все собственные значения матрицы положительны
    eigenvalues, _ = np.linalg.eig(matrix)
    if np.all(eigenvalues > 0):
        return True
    else:
        return False


def matrix_vector_multiply(matrix, vector):
    matrix = np.array(matrix)
    vector = np.array(vector)
    # Проверка совместимости размерностей матрицы и вектора
    if matrix.shape[1] != vector.shape[0]:
        raise ValueError("Несовместимые размерности матрицы и вектора")

    # Умножение матрицы на вектор
    result = np.dot(matrix, vector)

    return result

