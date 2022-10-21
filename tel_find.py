import csv

csvfile = 'base.csv'

def find_data(field, name_string):
    reader = {}
    result_search = []
    with open(csvfile, 'r', encoding="utf-8") as file:

        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row[field] == name_string:
                result_search += row.values()
        if result_search == []:
            print('данные в БД не найдены')
        return result_search