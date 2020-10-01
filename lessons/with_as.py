# Конструкция with ... as используется для оборачивания выполнения блока инструкций менеджером контекста.
#with <Выражение>[ as <Переменная>]:
    #<Блок, в котором перехватываем исключения>

# читаем все строки. fin значение возвращаемое open. with open(...) as fin связывает fin со значением,
# которое возвращает неявный вызов метода __enter__().
with open('text.txt') as fin:
    for line in fin:
        print(line)

# читаем первую строчку, потом остальные
with open('text.txt') as fin:
    line = next(fin)
    print('first line:', line)

    for line in fin:
        print(line)