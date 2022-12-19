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

if __name__ == '__main__':
    bond_list = reader()
    bond_list = sorter(bond_list)
    writer(bond_list)


