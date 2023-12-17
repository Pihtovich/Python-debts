# Задание 1-е
# Задан список с числами. Напишите программу, которая меняет
# местами наибольший и наименьший элемент и выводит новый список.

hello_str = "Введите последовательность чисел: "
in_lst = [int(item) for item in input(hello_str).split()]
print(in_lst)

max_elem, min_elem = max(in_lst), min(in_lst)
index1, index2 = in_lst.index(max_elem), in_lst.index(min_elem)
in_lst[index1], in_lst[index2] = in_lst[index2], in_lst[index1]
print(in_lst)


