# Реализовать кодирование длин серий (Run-length encoding).
# Дан вектор x. Необходимо вернуть кортеж из двух векторов одинаковой длины.
# Первый содержит числа, а второй - сколько раз их нужно повторить.
import numpy as np


def run_length_encoding_1(x):
    dict = {}
    for key in x:
        dict[key] = dict.setdefault(key, 0) + 1
    return (np.array(list(dict.keys())),
            np.array(list(dict.values())))


vcr = np.array(list(map(int, input().split())))
print(run_length_encoding_1(vcr))




