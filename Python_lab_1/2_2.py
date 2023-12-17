# Напишите программу, в которой задается натуральное число n и
# выводится пирамида из n ступенек, i-я ступень должна состоять из чисел
# от 1 до i и обратно без пробелов.

def build_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()


n = int(input("Введите кол-во ступенек: "))
build_pyramid(n)