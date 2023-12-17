# Задание 1-е
# Считать из файла input.txt 10 чисел (числа записаны через пробел).
# Затем записать их произведение в файл output.txt.
def get_composition(_lst):
    comp = 1
    for i in range(len(_lst)):
        comp *= _lst[i]
    return comp


fin = open("input_6_1.txt", "r")
in_lst = fin.readline().split()
fin.close()

lst = list(map(int, in_lst))
f = open('output_6_1.txt', 'w')
f.write(str(get_composition(lst)))
fin.close()
