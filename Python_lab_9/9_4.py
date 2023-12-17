# Найти максимальный элемент в векторе x
# среди элементов, перед которыми стоит нулевой.
# Для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.
import numpy as np

s = "Введите к-ты вектора через пробел: "
lst = list(map(int, input(s).split()))
x = np.array(lst)

num = np.where(x[:-1] == 0)[0]
max_element = np.max(x[num + 1])
print(max_element)