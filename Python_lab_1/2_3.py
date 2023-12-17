def print_modified_triangle(n):
    for i in range(0, n):
        num = 1
        for j in range(0, i + 1):
            print(num, end=" ")
            num += 1
        print("\r")


def print_modified_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end=' ')
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


n = int(input("Введите число: "))
print_modified_pyramid(n)
print_modified_triangle(n)