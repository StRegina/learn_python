# Объектно-ориентированное программирование (ООП) — парадигма программирования,
# в которой основными концепциями являются понятия объектов и классов.
# Класс — тип, описывающий устройство объектов.
# Объект — это экземпляр класса.

class A:
    pass
a = A()
b = A()
a.arg = 1  # у экземпляра a появился атрибут arg
b.arg = 2
print(a.arg)
print(b.arg)

class A:
    def g(self):
        return 'Hello world!'
a = A()
a.g()

class B:
    arg = 'Python'
    def g(self):
        return self.arg
b = B()
b.g()
B.g(b)
b.arg = 'Haribo' # переименование
b.g() 
