
def single_root_words (root_word, *other_words):
    same_words = [] # пустой список для хранения однокоренных слов
    for word in other_words: # Перебираем слова из other_words
        if root_word in word or word in root_word:
            same_words.append(word) # Если условие выполнено, добавляем слово в список same_words
    return same_words # Возвращаем список однокоренных слов
# Примеры вызова функции из задания
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на консоль
print(result1)
print(result2)