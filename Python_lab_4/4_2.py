# Задание 2
# Напишите программу, которая принимает 2 списка чисел и
# определяет количество общих чисел из первого и второго списка.
def get_count_general_elem_of_lists(lst1, lst2):
    if len(lst1) >= len(lst2):
        lst1, lst2 = lst2, lst1

    count = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                count += 1
    return count


hello_str = "Введите последовательность чисел: "
in_lst1 = [int(item) for item in input(hello_str).split()]
in_lst2 = [int(item) for item in input(hello_str).split()]
print("Списки:", in_lst1, in_lst2)
result = get_count_general_elem_of_lists(in_lst1, in_lst2)
print("К-во общих элементов списков: ", result)


