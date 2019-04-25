# Написать функцию, котоая возвращает кол-во строчных букв (пропускает заглавные)

def f1(a):
    s = 0
    for i in range(len(a)):
        if 97 <= ord(a[i]) <= 122 or 1072 <= ord(a[i]) <= 1103:
            s += 1
    return s


def f2(a):
    s = 0
    return len([s + 1 for i in range(len(a)) if 97 <= ord(a[i]) <= 122 or 1072 <= ord(a[i]) <= 1103])


a = input()
print(f1(a), f2(a))
