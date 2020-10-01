# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
a = {}
b = {'dict': 1}
c = dict(home='one', room='two')
d = dict([(1, 5), (3, 9)])
f = dict.fromkeys(['a', 'b']) # присваевается значение None
g = dict.fromkeys(['a', 'b'], 100) # присваевается значение 100
w = {a: a ** 2 for a in range(7)} # создается словарь по 7 число не включительно

r = {1: 2, 2: 4, 3: 9}
r[1]
r[4] = 4 ** 2 # добавится четвертое значение, которое удет равно 4 во 2 степени

s = {1: 2, 2: 4, 3: 9}
s.clear() # очищает словарь
s.copy() # возвращает копию словаря
s.items() # возвращает пары (ключ, значение).
s.keys() # возвращает ключи в словаре.
s.popitem() # удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError
s.values() # возвращает значения в словаре.
