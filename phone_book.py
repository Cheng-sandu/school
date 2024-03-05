import csv

with open('FIOandTelephone.csv', 'r', encoding='utf-8-sig') as files:
    reader=csv.DictReader(files)
    FIO=input("Ввелите ФИО")
    for row in reader:
        if FIO==row['FIO']:
            print("телефон:", row["Telephone"])
        else:
            continue