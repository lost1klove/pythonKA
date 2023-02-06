# Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции
# +,-,/,* приоритет операций стандартный.
# * Добавьте скобки,  приоритет операций меняется.

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


def sort_s(string):
    splt = string.split()
    fnl_splt = []
    i = 0
    while i < len(splt):
        if splt[i] == '(':
            brck = splt.index(')')
            fnl_splt.append(splt[i + 1:brck])
            i = brck
        else:
            fnl_splt.append(splt[i])
        i += 1
    return fnl_splt


def calc(any_list):
    for i, v in enumerate(any_list):
        if isinstance(v, list):
            any_list[i] = calc(v)
    ch = [i for i, v in enumerate(any_list) if v in '*/']

    while ch:
        temp = ch[0]
        a, b, c = any_list[temp - 1:temp + 2]
        any_list.insert(temp - 1, actions[b](a, c))
        del any_list[temp:temp + 3]
        ch = [i for i, v in enumerate(any_list) if v in '*/']
    while len(any_list) > 1:
        a, b, c = any_list[:3]
        del any_list[:3]
        any_list.insert(0, actions[b](a, c))
    return any_list[0]


# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# # exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# # exp = "( 12 + 8 ) * 3 - 11 / 2".split()
# # exp = "11 / 2 - ( 12 + 8 ) * 3".split()
# # exp = "5 + 11 / 2 - ( 12 + 8 ) * 3 - 12".split()
# # exp = "4 * ( 3 - 1 ) / ( 9 - 7 ) * -1".split()
# # exp = "8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )".split()

d = input('Введите выражение : ')

print(sort_s(d))
print(calc(sort_s(d)))
