import math


def square(a):
    return math.ceil(a * a)


a = float(input("Введите сторону квадрата: "))
s = square(a)

print("Площадь квадрата: ", s)
