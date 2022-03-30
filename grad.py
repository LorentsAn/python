# выбираем точку 1\(2sqrt(2)e^1/4)
# u(x, y) = x^2y^2ln(4x^2+y^2)

import math
import time
import numpy as np
import matplotlib.pyplot as plt

count = 0


def func(x, y):
    return (x ** 2) * (y ** 2) * math.log(4 * (x ** 2) + (y ** 2))


def grad(x, y, a):
    derivative_for_x = (-1) * 2 * x * (y ** 2) * (
            math.log(4 * (x ** 2) + (y ** 2)) + 4 * (x ** 2) / (4 * (x ** 2) + (y ** 2)))
    derivative_for_y = (-1) * 2 * y * (x ** 2) * (
            math.log(4 * (x ** 2) + (y ** 2)) + (y ** 2) / (4 * (x ** 2) + (y ** 2)))
    ab = [a * derivative_for_x + x, a * derivative_for_y + y]
    return ab


def calculate(last_value, a):
    global count
    count += 1
    global point
    global last_increment
    new_point = grad(point[0], point[1], a)
    value = func(new_point[0], new_point[1])
    if value < last_value:
        a /= 1.0001
        last_increment = last_value - value
    else:
        a /= 1.0001
    if last_increment < e:
        return count
    point = new_point
    plt.scatter([point[0]], [point[1]])
    calculate(value, a)


timing = time.time()
e = 0.00000000000000001
point = [1 / 2, 1 / 2]
last_increment = math.inf
last_value = func(1 / 2, 1 / 2)
a = 0.95
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
z = (x ** 2) * (y ** 2) * np.log(4 * (x ** 2) + (y ** 2))

ax.plot_surface(x, y, z)

fig2 = plt.figure()

calculate(last_value, a)
val = func(point[0], point[1])
ax.scatter(point[0], point[1], val, c="red")
plt.grid()
true_x = 1 / (2 * math.sqrt(2) * math.e ** (1 / 4))
true_y = 1 / (math.sqrt(2) * math.e ** (1 / 4))
print("Критерий останова:", e, "\nЧисло итераций:", count, "\nПолученная точка: (", point[0], point[1],
      ") \nПолученное значение:", val, "\nВремя работы:", time.time() - timing, "\nТочность вычисления точки до",
      math.fabs(true_x - point[0]), "и", math.fabs(true_y - point[1]), "\nТочность вычисления значения до",
      math.fabs(val - func(true_x, true_y)))
plt.show()
