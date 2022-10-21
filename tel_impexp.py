txtfile = 'base.txt'
csvfile = 'base.csv'

def import_to_csv():
    import csv

    with open(txtfile, 'r', encoding="utf-8") as infile, open(csvfile, 'a', encoding="utf-8") as outfile:
        lines = infile.readlines()
        for line in lines:
            writer = csv.writer(outfile, lineterminator='\n', delimiter=';')
            writer.writerow((line.strip()).split(sep=';'))


def export_to_txt():
    import csv

    with open(csvfile, 'r', encoding="utf-8") as infile, open(txtfile, 'w', encoding="utf-8") as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        for row in reader:
            outfile.writelines((';'.join(row.values())))
            outfile.writelines('\n')
