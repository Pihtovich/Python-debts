import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Задание 1-е
# Используя модуль scipy.signal и numpy сгенерировать
# и отрисовать с помощью matplotlib прямоугольный сигнал.

t = np.linspace(0, 1, 1000, endpoint=False)
wave = signal.square(2 * np.pi * 10 * t)

plt.plot(t, wave)
plt.show()
