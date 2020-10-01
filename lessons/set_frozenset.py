# Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет
a = set()
a = set('hello')
a = {'a', 'b', 'c', 'd'}
a = {i ** 2 for i in range(10)} # генератор множеств (числа с 0 по 9 возводятся во вторую степень)
type(a) # можно узнать тип

words = {'hello', 'world', 'hello', 'home'}
set(words) # удаляет повторяющееся слово
other = {'hello', 'mum'}

len(words) # считает число элементов в множестве
'hello' in words # принадлежит ли 'hello' множеству words
words.isdisjoint(other) # истина, если set и other не имеют общих элементов.
words == other # все элементы set принадлежат other, все элементы other принадлежат set.
words.issubset(other) # set <= other - все элементы set принадлежат other.
words.issuperset(other) # set >= other - аналогично.
words.union(other) # объединение нескольких множеств.
words.intersection(other) # пересечение (какое множество повторяется)
words.difference(other) # множество из всех элементов words, не принадлежащие ни одному из other.
words.symmetric_difference(other) # множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
words.copy() # копия множества.

print(words.isdisjoint(other))

words.update(other) # объединение
words.intersection_update(other) # пересечение.
words.difference_update(other) # вычитание.
words.symmetric_difference_update(other) # множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
words.add('elem') # добавляет элемент в множество.
words.remove('elem') # удаляет элемент из множества. KeyError, если такого элемента не существует.
words.discard('elem') - удаляет элемент, если он находится в множестве.
words.pop() # удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
words.clear() # очистка множества.

a = set('words')
b = frozenset('words')
a == b
type(a - b)
type(a | b)
a.add(1) # можно изменить
b.add(1) # нельзя изменить