# Напишите программу, которая принимает список строк и выводит
# количество повторений данных строк в списке.
# Необходимо реализовать решение с использованием словарей.
# Входные данные: ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc'].
# 1)Выходные данные: 3 1 2 1.
# 2) Входные данные: ['aaa', 'bbb', 'ccc'].
# Выходные данные: 1 1 1.
# 3) Входные данные: ['abc', 'abc', 'abc'].
# Выходные данные: 3.
def get_dictionary_from_list(lst):
    dictionary = dict.fromkeys(lst, 0)
    for s in lst:
        dictionary[s] = dictionary.get(s) + 1
    return [*dictionary.values()]


in_lst = []
length = int(input("Введите длину списка строк: "))
for i in range(length):
    in_lst.append(input(f"Строка номер {i + 1}: "))

result = get_dictionary_from_list(in_lst)
print(*result, sep=' ')


