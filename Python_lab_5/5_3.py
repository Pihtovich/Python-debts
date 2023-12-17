# Задание 3-е
# Саша и Маша играют в игру города. Они очень любят эту игру,
# однако к концу игры  забывают, какие города уже называли.
# Напишите программу, считывающую информацию об игре и сообщающую ребятам,
# что очередной город назван повторно.

# ---Формат входных данных
# На вход программе в первой строке подаётся натуральное число n – количество
# названных городов, в последующих n строках вводятся названные города
# и ещё одна строка с новым, только что названым городом.

# ---Формат выходных данных
# Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT,
# если город уже был назван.

n = int(input("Количество названных городов: "))

in_lst = []
for i in range(1, n + 1):
    in_str = input("Город " + str(i) + "-ый: ").replace(' ', '')
    in_lst.append(in_str)
plenty = set(in_lst)

print(plenty)
town = input("Еще один город: ")
if town in plenty:
    print("REPEAT")
else:
    print("OK")

