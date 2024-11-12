import string
from collections import defaultdict


def analyze_text(text):
    # Приводим текст к нижнему регистру и удаляем знаки препинания
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Разбиваем текст на слова
    words = text.split()

    # Создаем словарь для подсчета частоты слов
    word_count = defaultdict(int)

    # Подсчитываем частоту каждого слова
    for word in words:
        word_count[word] += 1

    # Преобразуем словарь в список кортежей и сортируем
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    # Выводим результаты
    for word, count in sorted_words:
        print(f"{word}: {count}")


# Ввод текста от пользователя
user_input = input("Введите текст: ")
analyze_text(user_input)
