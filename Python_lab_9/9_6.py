# Поменять местами две строки в двумерном массиве NumPy -
# поменяйте строки 1 и 3 массива а.
# a = np.arange(16).reshape(4,4)
import numpy as np

arr = np.arange(16).reshape(4, 4)
print(f"Старый двумерный массив:\n {arr}\n")

copy_arr = arr.copy()
copy_arr[0], copy_arr[3] = copy_arr[3], copy_arr[0]
print(f"Новый двумерный массив: \n{copy_arr}")