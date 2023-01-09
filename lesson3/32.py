# 1. Задайте список, состоящий из произвольных слов, \
# 2.количество задаёт пользователь.
# 3. Напишите программу, которая
# 4. определит индекс второго вхождения строки в списке
# 5. либо сообщит, что её нет.

from random import sample


def words_list(words_amount, word='abc'):
    w_list = []
    for i in range(words_amount):
        m = sample(word, k=3)
        w_list.append("".join(m))
    return w_list


def find_second(m_list, word):
    if word in m_list and m_list.count(word) > 1:
        c = m_list.index(word)
        print(m_list.index(word, c+1))
    else:
        print(-1)


n = int(input('Введите число : '))
lists = words_list(n)
print(lists)
w = input("Введите слово : ")
find_second(lists, w)
