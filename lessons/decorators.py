# функции в python являются объектами, т.е. их можно возвращать из другой функции или
# передавать в качестве аргумента. функция в python может быть определена и внутри другой функции.
# Декораторы — это "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.
def my_shiny_new_decorator(function_to_decorate): # мой новый блестящий декоратор (функция украшения)
    def the_wrapper_around_the_original_function(): # обертка вокруг оригинальной функции
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function

# функция, которую не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

stand_alone_function()
# чтобы изменить её поведение, можно декорировать её
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()

stand_alone_function = my_shiny_new_decorator(stand_alone_function) # перезаписываем
stand_alone_function()

# простой вариант:

def my_shiny_new_decorator(function_to_decorate): # мой новый блестящий декоратор (функция украшения)
    def the_wrapper_around_the_original_function(): # обертка вокруг оригинальной функции
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")

another_stand_alone_function()



def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()




def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_full_name("Vasya", "Pupkin")



def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)
    return wrapper

class Lucy:
    def __init__(self):
        self.age = 32
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

l = Lucy()
l.sayYourAge(-3)