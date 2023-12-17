# 5. Реализовать функцию вычисления логарифма плотности многомерного
# нормального распределения.Входные параметры: точки X, размер (N, D),
# мат. ожидание m, вектор длины D, матрица ковариаций C, размер (D, D).
# Разрешается использовать библиотечные функции для подсчета определителя матрицы,
# а также обратной матрицы, в том числе в невекторизованном варианте.
# Сравнить с scipy.stats.multivariate_normal(m, C).logpdf(X) как по скорости работы,
# так и по точности вычислений.

import numpy as np
from scipy.stats import multivariate_normal
import time


def log_density(x, m, c):
    d = len(m)
    det = np.linalg.det(c)
    inv = np.linalg.inv(c)
    diff = x - m
    exponent = -0.5 * np.sum(diff.dot(inv) * diff, axis=1)
    normalization = -0.5 * d * np.log(2 * np.pi) - 0.5 * np.log(det)
    log = exponent + normalization
    return log


n, d = 5, 10
x = np.random.randn(n, d)
m = np.random.randn(d)
c = np.random.randn(d, d)
c = np.dot(c, c.T)

start1 = time.time()
log = log_density(x, m, c)
print(log)
final_time1 = time.time() - start1

start2 = time.time()
log2 = multivariate_normal(m, c).logpdf(x)
print(log2, "\n")
final_time2 = time.time() - start2

print(f'Время выполнения своей функции: {final_time1}')
print(f'Время выполнения с помощью scipy.stats.multivariate_normal: {final_time2}')