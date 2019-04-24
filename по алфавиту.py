def f(a):
    d = dict()
    for letter in a.lower():
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    k = ''
    for i in range(25, 122):
        letter = chr(i)
        if letter in d:
            k += letter * (d.get(letter))
    return k


a = input()
print(f(a))

