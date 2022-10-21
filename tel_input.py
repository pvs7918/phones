base_csv = 'base.csv'

def input_data():
    import csv
    head = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    values = []
    for i in head:
        enter = input(f'Введите {i} ')
        if i == head[3]:
            if enter.isdigit() == False:
                print('Поле должно быть числом')
                break
        else:
            if enter.isalpha() == False:
                print('Поле должно быть текстом')
                break
        values.append(enter)
    if len(values) == 4:
        with open(base_csv, 'a', encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n', delimiter=';')
            writer.writerow(values)
