print("Hello world!")
print(2+2)
print(12-7)
print(2*3)
print(2**4)
print(5/2)
# Получение целой части от деления
print(5//2)
# Остаток от деления
print(5%2)
# 3 в 4 степени по модулю
pow(-3,4)

a = 150
b = 12.9
a+b
c = abs(b - a)
print(c)
round(c)

# Вставить в консоль, нажать enter, ввести имя, нажать enter
name = input("Как вас зовут? ")
print("Привет,", name)

a = int(input()) + 5

# Модуль math предоставляет более сложные математические функции.
import math
math.pi
math.sqrt(81)
math.sqrt(50)

# Модуль random реализует генератор случайных чисел и функции случайного выбора.
import random
random.random()

# Комплексные числа, где a, b — вещественные числа, i — мнимая единица, j^2 = -1
x = complex(1,2)
print(x)
y = complex(3,4)
print(y)
z = x + y
print(z)
z = x * y
print(z)
z = x / y
print(z)
# Сопряжённое число
print(x.conjugate())
# Мнимая часть
print(x.imag)
# Действительная часть
print(x.real)