import numpy as np


def f(x):
    return np.exp(-x**2)


def simpson_composite(f, a, b, n):
    h = (b - a) / n
    x0 = a
    I = f(x0)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 != 0:
            I = I + 4 * f(x_i)
        else:
            I = I + 2 * f(x_i)
    xn = b
    I = I + f(xn)
    I = I * h / 3
    return I


a, b = 0, 1
n = int(input("Entre le nombre de subdivisions (pair) : "))
while n % 2 != 0:
    n = int(input("n doit être pair, réessaie : "))

print("Intégrale ≈", simpson_composite(f, a, b, n))
