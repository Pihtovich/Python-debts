import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Задание № 1
# Вывести на один график, разными цветами графики полиномов Лежандра
# различных степеней (от 1 до 7). Задать заголовок изображения как «Полиномы Лежандра».
# Реализовать легенду графика в виде выносок от каждого полинома на графике с указанием степени
# ( - n = 3 как пример). Для реализации полиномов использовать ScyPy.
degrees = range(1, 8)

figure, axes = plt.subplots()

for d in degrees:
    x = np.linspace(-1, 1, 100)
    y = legendre(d)(x)
    axes.plot(x, y, label=f'n = {d}')

axes.set_title('Полиномы Лежандра')
axes.legend()
plt.show()
