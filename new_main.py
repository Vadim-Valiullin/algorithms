import csv


def reader():
    with open('all_stocks_5yr.csv', newline='') as File:
        reader = csv.reader(File)
        bond_list = []
        count = 0
        for row in reader:
            if 0 < count <= 10:
                bond_list.append(row)
            count += 1
        return bond_list


def sorter(bond_list):
    flag = True
    while flag:
        flag = False
        for i in range(len(bond_list)-1):
            if bond_list[i][2] > bond_list[i+1][2]:
                bond_list[i][2], bond_list[i+1][2] = bond_list[i+1][2], bond_list[i][2] # сортируем список по колонке
                # high по-возростанию
                flag = True
    return bond_list


def writer(bond_list):
    with open("new_file.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(bond_list)
        
        
        
def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    with open('all_stocks_5yr.csv', newline='') as File:
        reader = csv.reader(File)
        bond_list = []
        for row in reader:
            if row[0] == date and row[6] == name:
                bond_list.append(row)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(bond_list)
        
        
columns_hash_table = {'date':0, 'open':1, 'high':2, 'low':3, 'close':4, 'volume':5, 'Name':6}
cash_file = {}

def input_name_column(bond_list):
    while True:
        input_column = input('Введите название колонки по которой требуется сортировка: ')
        if not input_column in columns_hash_table:
            print('Вы ввели несуществующее название колонки!')
            continue
        else:
            if cash_file.get(input_column):
                with open(f'dump_{input_column}.csv', newline='') as File:
                    reader = csv.reader(File)
                    with open(f"dump_{input_column}1.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(reader)
            else:
                with open(f"dump_{input_column}.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(bond_list)
                    cash_file[input_column] = f"dump_{input_column}.csv"
        print(f'Содержимое кэша: {cash_file}')


if __name__ == '__main__':
    bond_list = reader()
    input_name_column(bond_list)
#     bond_list = sorter(bond_list)
#     writer(bond_list)
#     get_by_date()


