import json
import os
import csv
# Написать программу на Python преобразующую json файл  в CSV.
# Входной параметр  – имя json файла. Результирующий CSV файл должен иметь название
# из названия записи json и размещаться  в той же папке что и json.
# Формат вызова программы в командной строке: json2csv.py example.json
# Примеры Json файлов и краткая теория по работе с json прилагаются к заданию.

def json2csv(_filename):
    with open(_filename, 'r') as j:
        json_data = json.load(j)

    _filename = os.path.splitext(_filename)[0]
    csv_file = f"{_filename}.csv"
    with open(csv_file, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(json_data['users'][0].keys())
        for item in json_data['users']:
            writer.writerow(item.values())


filename = input("Введите название файла: ")
json2csv(filename)