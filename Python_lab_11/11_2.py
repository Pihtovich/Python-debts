import numpy as np
import matplotlib.pyplot as plt

# Задание 2-ое
# Используя  numpy сгенерировать  и отрисовать с помощью
# matplotlib в виде гистограммы нормальное распределение.

mid, std, size = 0, 1, 10000

samples = np.random.normal(mid, std, size)
plt.hist(samples, bins=30, density=True)
plt.show()
