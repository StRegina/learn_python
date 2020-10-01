# Выполняет тело цикла до тех пор, пока условие цикла истинно.
i = 5
while i < 15:
    print(i)
    i = i + 1

#  цикл проходится по любому итерируемому объекту (например строке или списку), и во время каждого прохода выполняет тело цикла.
for i in 'Hello world':
    print(i * 2, end = '')

# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
for i in 'Hello world':
    if i == 'o':
        continue
    print(i * 2, end = '')

# Оператор break досрочно прерывает цикл.
for i in 'Hello world':
    if i == 'o':
        break
    print(i * 2, end = '')

# Слово else, примененное в цикле for или while, проверяет, был ли произведен выход из цикла инструкцией break, или же "естественным" образом. Блок инструкций внутри else выполнится только в том случае, если выход из цикла произошел без помощи break.
for i in 'Hello world':
    if i == 'a':
        break
else:
    print('Буквы a в строке нет')