import csv

csvfile = "base.csv"

def search_data(field, name_string):
    reader = {}
    result_search = []
    with open(csvfile, 'r', encoding="utf-8") as file:

        reader = csv.DictReader(file)
        for row in reader:
            if row[field] == name_string:
                result_search += row.values()
        if result_search == []:
            print('данные в БД не найдены')
        return result_search