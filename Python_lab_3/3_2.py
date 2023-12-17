# 2-е задание
# Напишите программу, которая выводит 3 наиболее часто
# встречающихся символа (без учета пробелов) с указанием их количества
# в введенной пользователем строке
input_str = input().replace(' ', '')

x, count = {}, 0
for char in input_str:
    x[char] = x.get(char, 0) + 1
x = dict(sorted(x.items(), key=lambda item: -item[1]))

for i in list(x.keys())[0:3]:
    print(i, ':', x[i])

