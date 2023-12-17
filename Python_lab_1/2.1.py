# Напишите программу, в которой задается натуральное число n
# и выводится лестница из n ступенек, i-я ступенька должна
# состоять из чисел от 1 до i без пробелов.
# Необходимо решить в 2х вариантах, используя только числа и на основе строк

def build_triangle_with_num(num):
    for i in range(num):
        result, tmp = 0, i
        for j in range(1, i + 2):
            result += (10 ** tmp) * j
            tmp -= 1
        print(result)


def build_ladder_with_str(num):
    string = ""
    for i in range(1, num + 1):
        string += str(i)
        print(string)


num = int(input("Введите число: "))
build_triangle_with_num(num)
print()
build_ladder_with_str(num)