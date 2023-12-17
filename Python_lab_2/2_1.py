# Задаие № 1
# Напишите программу, которая выводит n строк треугольника Паскаля.
# https://ru.wikipedia.org/wiki/Треугольник_Паскаля
# Число n вводится с клавиатуры.
def pascal_triangle(num):
    lstNum = [[1]]
    for i in range(1, num + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if not(j == 0 or j == i):
                row[j] = lstNum[i - 1][j - 1] + lstNum[i - 1][j]
        lstNum.append(row)

    for row in lstNum:
        print(' ' *num, *row, sep=' ')
        num -= 1


print("==Треугольник Паскаля==")
countStr = int(input("Введите число строк: "))
pascal_triangle(countStr)



