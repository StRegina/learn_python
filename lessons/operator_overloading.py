# Перегрузка операторов — один из способов реализации полиморфизма,
# когда мы можем задать свою реализацию какого-либо метода в своём классе.
class A:
    def go(self):
        print('Go, A!')
a = A()
a.go()

class B(A):  # класс B наследует класс A, но переопределяет метод go
    def go(self, name):
        print('Go, {}!'.format(name)
b = B()
b.go('Ann')


class A:
    def __init__(self, name):
        self.name = name

a = A('Ann')
print(a.name)



import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Для вызова:
# x = Vector2D(2, 4)
# y = Vector2D(5, 6)
# x
# y

    def __repr__(self): # возвращает "сырые" данные, использующиеся для внутреннего представления в python.
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self): # Возвращает строковое представление объекта.
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other): # сложение
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other): # +=
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other): # вычитание
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other): # -=
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self): # модуль
        return math.hypot(self.x, self.y)

    def __bool__(self): # вызывается при проверке истинности
        return self.x != 0 or self.y != 0

    def __neg__(self): # унарный -
        return Vector2D(-self.x, -self.y)