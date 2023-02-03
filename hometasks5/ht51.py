# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#    В тексте используется разделитель пробел.

from random import sample


def delete_sent(words, deleter):
    return " ".join(words.replace(deleter, "").split())


def random_words(count: int, alp: str = 'абв'):
    list = []
    for i in range(count):
        symbols = sample(alp, 3)
        list.append("".join(symbols))
    return " ".join(list)


full_list = random_words(int(input("Введите количество слов : ")))
str_del = input('Введите набор символов, который нужно удалить из списка(одной строкой): ')
print(full_list)
print(delete_sent(full_list,str_del))
