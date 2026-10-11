import numpy as np


def f(x):
    return np.exp(-x**2)


def composite_trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    S = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        S = S + 2 * f(x)
    I = (h / 2) * S
    return I


a, b = 0, 1
n = int(input("Enter n: "))

print("Integral ≈", composite_trapezoidal_rule(f, a, b, n))
