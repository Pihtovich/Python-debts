# Задание 1-ое
# Допишите программу, которая принимает список чисел и, с помощью множеств,
# определяет количество различных чисел внутри списка.

def get_different_elements(lst):
    return len(set(lst))


in_lst = list(map(int, input().split()))
print(get_different_elements(in_lst))