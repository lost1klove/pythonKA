# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.


from itertools import groupby, starmap
from os import path


def encoder(text="words.txt", code_text="code_words.txt"):
    if path.exists(text):
        with open(text) as my_1, \
                open(code_text, "a") as my_2:
            for i in my_1:
                my_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Файла не существует!")


def decoder(name):
    if path.exists(name):
        with open(name) as my:
            n = ""
            for j in my:
                list = []
                for i in j.strip():
                    if i.isdigit():
                        n += i
                    else:
                        list.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, list)))
    else:
        print("Файла не существует!")

encoder(input("Введите имя файла с текстом : "), input("Введите имя файла для записи : "))
decoder(input("Введите имя файла для расшифровки : "))
