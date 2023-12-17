# 3-е задание
# Напишите программу, которая выводит текстовое написание числа.
# Число вводится пользователем в диапазоне от 1 до 1000.
# Например, при вводе числа 17 – выводится «семнадцать».
def get_digits(_num):
    digits = 0
    while _num != 0:
        _num //= 10
        digits += 1
    return digits


def get_registration_of_number(num):
    units = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
             6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
    between = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
               14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать",
               17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
    dozens = {10: "десять", 20: "двадцать", 30: "тридцать", 40: "сорок",
              50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят",
              80: "восемьдесят", 90: "девяносто"}
    hundreds = {100: "сто", 200: "двести", 300: "триста", 400: "четыреста",
                500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот",
                900: "девятьсот"}
    thousands = {1000: "тысяча"}
    dictionary = units | between | dozens | hundreds | thousands

    digits = get_digits(num)
    if num in dictionary:
        return dictionary.get(num)
    if digits == 2:
        return dictionary.get(num - num % 10) + ' ' + dictionary.get(num % 10)
    if digits == 3:
        if ((num // 10) % 10 == 0) or (num % 100 in dictionary):
            return dictionary.get(num - num % 100) + ' ' + dictionary.get(num % 100)
        result = dictionary.get(num - num % 100) + ' ' + dictionary.get(num % 100 - num % 10)
        return result + ' ' + dictionary.get(num % 100 % 10)


while True:
    num = input("Введите число: ")
    if num.isdigit() and (int(num) >= 1 and int(num) <= 1000):
        result = get_registration_of_number(int(num))
        print("Пропись числа '" + num + "':", result)
        break
    print("~Число некорректно...")
