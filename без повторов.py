def f(a):
    d = dict()
    s = ''
    for letter in a.lower():
        if letter not in d:
            s += letter
            d[letter] = 1
    return s


a = input()
print(f(a))
