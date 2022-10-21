import csv
import os.path

csvfile = 'base.csv'

import tel_impexp as impexp
import tel_input as inp
import tel_menu as mnu
import tel_find as srch


def main():
    mnu.main_menu('Begin')
    while True:
        mnu.main_menu('Main')
        value = input('Выберите пункт меню: ')
        if value.isdigit():
            value = int(value)
            if not (int(value) in range(5)):
                continue
            match value:
                case 1:
                    print('=' * 40)
                    mnu.file_menu()
                    value_1 = input('Подтвердите свой выбор ')
                    if value_1 == '1':
                        if os.path.exists(csvfile) == True:
                            print()
                            print('Файл уже существует!')
                            continue
                        with open(csvfile, 'w', encoding="utf-8") as file:
                            writer = csv.DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Телефон'],
                                                    lineterminator='\n', delimiter=';')
                            writer.writeheader()
                    else:
                        continue
                case 2:
                    print('=' * 40)
                    print('Ввод новой записи')
                    print('=' * 40)
                    if os.path.exists(csvfile) == False:
                        print()
                        print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                        continue
                    inp.input_data()
                case 3:
                    print('=' * 40)
                    print('Поиск записи')
                    print('=' * 40)
                    if os.path.exists(csvfile) == False:
                        print()
                        print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                        continue
                    mnu.find_menu()
                    value_1 = input('Выберите пункт ')
                    if value_1 == '1':
                        search_string = {}
                        name = input('Введите фамилию ')
                        if name.isalpha() == False:
                            print('Введено не верное значение')
                            continue
                        search_string = srch.find_data('Фамилия', name)
                    elif value_1 == '2':
                        search_string = []
                        name = input('Введите № телефона ')
                        if name.isdigit() == False:
                            print('Введено не верное значение')
                            continue
                        search_string = srch.find_data('Телефон', name)
                    else:
                        continue
                    print(search_string)
                case 4:
                    print('=' * 40)
                    print('Импорт/экспорт записей')
                    print('=' * 40)
                    mnu.imp_exp_menu()
                    value_1 = input('Выберите пункт ')
                    if value_1 == '1':
                        if os.path.exists(csvfile) == False:
                            print()
                            print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                            continue
                        impexp.export_to_txt()
                    elif value_1 == '2':
                        if os.path.exists(csvfile) == False:
                            print()
                            print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                            continue
                        impexp.import_to_csv()
                    else:
                        continue
                case 0:
                    break

main()