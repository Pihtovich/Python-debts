# Задание номер 1.0
# Напишите программу, которая принимает на вход строку
# символов (заглавные и прописные буквы латинского алфавита),
# которые могут повторятся, например: YYYYggkeeeAAABV .
# Заглавные и строчные буквы различаются.
# Программа должна преобразовать (закодировать) строку в сжатый формат:
# Y4g2ke3A3BV . Число после символа – количество повторений,
# если символ однократный – единицу выводить не надо.
def encode_to_short_format(in_str):
    tmp, out_str = in_str[0], ""
    for i in range(1, len(in_str)):
        if not in_str[i].isalpha():
            continue
        if in_str[i] == tmp[0]:
            tmp += in_str[i]
            continue
        if len(tmp) == 1:
            out_str += tmp[0]
        else:
            out_str += tmp[0] + str(len(tmp))
        tmp = in_str[i]
    if len(tmp) == 1:
        out_str += tmp[0]
    else:
        out_str += tmp[0] + str(len(tmp))
    return out_str


# Задание номер 1.1
# Напишите программу, которая решает обратную задачу по отношению к заданию 1.
# Из строки типа Y4g2ke3A3BV восстанавливает исходную.
def decode_to_full_format(in_str):
    out_str = ""
    for i in range(len(in_str) - 1):
        if in_str[i].isalpha() and in_str[i + 1].isdigit():
            out_str += in_str[i] * int(in_str[i + 1])
            continue
        if in_str[i].isalpha() and not in_str[i + 1].isdigit():
            out_str += in_str[i]
    if in_str[-1].isalpha():
        out_str += in_str[-1]
    return out_str


input_str = input("Введите строку символов: ")
output_str = encode_to_short_format(input_str)
print(output_str)
print("=" * 25)

input_str = input("Введите строку символов: ")
print(decode_to_full_format(input_str))