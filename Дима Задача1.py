def input_string():
    string1 = input("Введите 1-ю строку: ")
    string2 = input("Введите 2-ю строку: ")
    string3 = input("Введите 3-ю строку: ")
    return string1, string2, string3
def set_string(string1, string2, string3):
    string_set1 = set(string1.split())
    string_set2 = set(string2.split())
    string_set3 = set(string3.split())
    return string_set1, string_set2, string_set3
def filtration(string_set1, string_set2, string_set3):
    unique1 = string_set1.difference(string_set2, string_set3)
    unique2 = string_set2.difference(string_set1, string_set3)
    unique3 = string_set3.difference(string_set1, string_set2)
    all_strings = "#".join(unique1.union(unique2, unique3))
    return all_strings
def string_len(all_strings):
    lens = len(all_strings)
    return lens
def main():
    string1, string2, string3 = input_string()
    string_set1, string_set2, string_set3 = set_string(string1, string2, string3)
    all_strings = filtration(string_set1, string_set2, string_set3)
    lens = string_len(all_strings)
    print("Уникальные слова:", all_strings)
    print("Длина строки:", lens)


main()






