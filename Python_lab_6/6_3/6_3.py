# В текстовом файле записаны сведения о детях из детского сада
# в следующей форме (создать не менее 5 записей, с разным возрастом):
# Фамилия пробел Имя пробел возраст (Иванов Иван 5 )
# Необходимо записать в отдельные текстовые файлы самого старшего и самого младшего из них
in_dict = {}
with open("input_6_3.txt", "r", encoding='utf-8') as file1:
    for line in file1:
        string = line.rstrip()
        in_dict[line[:len(string) - 1]] = string[-1]
sort_dict = dict(sorted(in_dict.items(), key=lambda x: x[1], reverse=True))
file1.close()

print(sort_dict)

file2 = open("output_6_3.txt", "w", encoding='utf-8' )
lst = list(sort_dict.keys())

file2.write(lst[0] + str(sort_dict.get(lst[0])) + "\n")
file2.write(lst[-1] + str(sort_dict.get(lst[-1])))