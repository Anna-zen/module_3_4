
# Самостоятельная работа по уроку "Произвольное число параметров".
# Задача "Однокоренные":
def single_root_words (root_word, *other_words) :

    root_word = root_word.lower()       # приводим слова к нижнему регистру
    other_words = [word.lower() for word in other_words]

    same_words = []   # Создаем пустой список для хранения совпадающих слов

    for word_i in other_words:                      # Перебираем все слова из других слов
        if root_word in word_i or word_i in root_word:
            same_words.append(a)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)