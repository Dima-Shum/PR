def get_input_strings():
    strings = []
    while True:
        user_input = input("Введите строки слов через дефис (или 'HELLO' для выхода): ")
        if 'HELLO' in user_input:
            break
        strings.append(user_input)
    return strings


def filter_words(strings):
    target_word = "computer"
    target_letter_set = set(target_word)
    filtered_strings = []
    for index, string in enumerate(strings):
        words = [word.strip() for word in string.split('-')]
        unique_words = set(words)
        valid_words = set()
        for word in unique_words:
            common_letters = len(set(word) & target_letter_set)
            if common_letters <= 3:
                valid_words.add(word)

        sorted_words = sorted(valid_words, reverse=True)

        if index % 3 == 0:
            sorted_words = [word.upper() for word in sorted_words]  # Поменяли на нужный уровень

        filtered_strings.append(" ".join(sorted_words))
    return filtered_strings


def main():
    strings = get_input_strings()
    if strings:
        filtered_strings = filter_words(strings)
        print("\nРезультат:")
        for result in filtered_strings:
            print(result)
    else:
        print("\nНе введено ни одной строки.")


# Запуск программы
main()