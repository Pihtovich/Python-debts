import numpy
import matplotlib.pyplot
from matplotlib.widgets import Slider

# Задание 4-е
# Реализовать с помощью Matplotlib блок моделирования сложения 2 волн,
# включающий 2 интерактивных окна для задания исходных волн (как sin(x))
# минимальная интерактивность включат 2 слайдера регулирующих частоту и
# амплитуду волны. Кроме 2 интерактивных  окон должно присутствовать
# окно отображающее результат сложения 2х волн

fig, (ax_1, ax_2, ax_3) = matplotlib.pyplot.subplots(3, 1, figsize=(8, 6))

freq1, freq2 = 1.0, 2.0
amp1, amp2 = 1.0, 0.5

x = numpy.linspace(0, 10, 1000)


def wave(x, frequency, amplitude):
    return amplitude * numpy.sin(2 * numpy.pi * frequency * x)


wave1 = wave(x, freq1, amp1)
wave2 = wave(x, freq2, amp2)
sum_wave = wave1 + wave2

# Отображение волн на графиках
line1, = ax_1.plot(x, wave1, label='Волна 1')
line2, = ax_2.plot(x, wave2, label='Волна 2')
line3, = ax_3.plot(x, sum_wave, label='Сложение волн')

# Создание слайдеров для регулировки параметров волн
axcolor = 'lightgoldenrodyellow'
ax_freq1 = matplotlib.pyplot .axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_amp1 = matplotlib.pyplot .axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_freq2 = matplotlib.pyplot .axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_amp2 = matplotlib.pyplot .axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

slider_freq1 = Slider(ax_freq1, 'Частота 1', 0.1, 10.0, valinit=freq1)
slider_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1)
slider_freq2 = Slider(ax_freq2, 'Частота 2', 0.1, 10.0, valinit=freq2)
slider_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2)


def wave(x, frequency, amplitude):
    return amplitude * numpy.sin(2 * numpy.pi * frequency * x)


# Функция для обновления графиков при изменении параметров волн
def update(val):
    freq1 = slider_freq1.val
    amp1 = slider_amp1.val
    freq2 = slider_freq2.val
    amp2 = slider_amp2.val

    wave1 = wave(x, freq1, amp1)
    wave2 = wave(x, freq2, amp2)
    sum_wave = wave1 + wave2

    line1.set_ydata(wave1)
    line2.set_ydata(wave2)
    line3.set_ydata(sum_wave)

    fig.canvas.draw_idle()

slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)

# Настройка графиков
ax_1.set_title('Волна 1')
ax_1.set_xlabel('x')
ax_1.set_ylabel('y')
ax_1.legend()

ax_2.set_title('Волна 2')
ax_2.set_xlabel('x')
ax_2.set_ylabel('y')
ax_2.legend()

ax_3.set_title('Сложение волн')
ax_3.set_xlabel('x')
ax_3.set_ylabel('y')
ax_3.legend()

matplotlib.pyplot .show()