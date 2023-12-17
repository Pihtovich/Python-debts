# задание 0
# Задан список с числами. Напишите программу, которая выводит
# все элементы списка, которые больше предыдущего, в виде отдельного списка.

# вариант 1-й
hello_str = "Введите последовательность чисел: "
in_lst = [int(item) for item in input(hello_str).split()]
out_lst = [j for i, j in zip(in_lst, in_lst[1:]) if j > i]
print(out_lst)
