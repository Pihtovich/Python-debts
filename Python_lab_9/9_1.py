# Прочитать матрицу из файла.
# Найдите для этой матрицы сумму всех элементов,
# максимальный и минимальный элемент (число)
import numpy as np

matrix = np.ones((3, 4), int)
with open('8_2.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    lines[i] = lines[i].replace(',', ' ')
    matrix[i] = list(map(int, lines[i].split()))
print(matrix)

print("Sum of matrix:", np.sum(matrix))
print("Sum of matrix:", np.min(matrix))
print("Sum of matrix:", np.max(matrix))

