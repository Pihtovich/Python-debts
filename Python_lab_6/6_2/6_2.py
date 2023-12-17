# Дан файл в котором записаны в столбик (каждое на отдельной строке)
# целые числа, всего 10 чисел. Отсортировать их по возрастанию цифр
# и записать в другой файл.
in_lst = []
with open("input_6_2.txt", "r") as file1:
    for line in file1:
        in_lst.append(line.strip())
file1.close()

out_lst = list(map(int, in_lst))
out_lst.sort()

file2 = open("output_6_2.txt", "w")
for i in range(len(out_lst)):
    file2.write(str(out_lst[i]) + " ")
file2.close()


