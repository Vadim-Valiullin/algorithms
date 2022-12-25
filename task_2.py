# Результат : 7
# Семь различных подстрок: "", "g", "f", "gf", "fg", "gg", "gfg"
str_1 = "gfg"


def variations(str_1):
    list_1 = []
    list_1.append(str_1)
    list_str_1 = list("gfg")
    for i in range(len(list_str_1)-1):
        if list_str_1[i] in str_1 and list_str_1[i] not in list_1:
            list_1.append(list_str_1[i])
        if list_str_1[i] + list_str_1[i-1] not in list_1:
            list_1.append(list_str_1[i] + list_str_1[i-1])
        if list_str_1[i] + list_str_1[i+1] not in list_1:
            list_1.append(list_str_1[i] + list_str_1[i+1])
        if '' not in list_1:
            list_1.append('')

    return list_1


print(variations(str_1))


# Результат : 4
# Четыре различных подстроки: "", "g", "gg", "ggg"

str_2 = "ggg"

def list_variations(str_2):
    list_str_2 = list(str_2)
    char = ''
    list_of_variations = []
    for i in range(len(list_str_2)):
        if list_of_variations == []:
            list_of_variations.append(char)
        list_of_variations.append(str_2[i] * (i+1))

    return list_of_variations

print(list_variations(str_2))
