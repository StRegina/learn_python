# кортеж защищен от изменений, как намеренных, так и случайных
a = (1, 2, 3, 4, 5, 6)
a.__sizeof__()

b = [1, 2, 3, 4, 5, 6]
b.__sizeof__()

c = {(1,2,3):1} # использование кортежа в качестве ключей словаря

d = tuple() # пустой кортеж
f = () # пустой кортеж

g = ('34') # так получится строка
g = ('34',) # так получится котреж из одного элемента

h = tuple('hello, world!') # создание кортежа

k = (1, 2, 3, 4, 5, 6)
l = (7, 8, 9)
k,l = l,k # кортежи поменяются местами