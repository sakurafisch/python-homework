import csv

file_path: str = input('Enter subject file name: ')
column_length1: int = int(input('Enter 1st column length: '))
column_length2: int = int(input('Enter 2nd column length: '))
column_length3: int = int(input('Enter 3rd column length: '))
with open(file_path, 'r') as file:
    reader: csv.DictReader = csv.DictReader(file)
    code: str = 'code'
    name: str = 'name'
    cp: str = 'cp'
    print(f"{code.title():<{column_length1}}{name.title():^{column_length2}}{cp.upper():>{column_length3}}")
    for row in reader:
        code_value = row.get(code)
        name_value = row.get(name)
        cp_value = row.get(cp)
        print(f"{code_value:<{column_length1}}{name_value:^{column_length2}}{cp_value:>{column_length3}}")


