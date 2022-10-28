def hello_world():
    print("hi")
    return 'Hello World'


# a = hello_world
# print(a)
#
# my_list = [a, a, a]
# my_list[0]()


def caller(some_func):
    def generated_func():
        print(f"указано название функции {some_func}")
        print("ниже она будет вызвана 2 раза")
        some_func()
        some_func()
        print("конец функции")

    return generated_func  # не указали скобки


# x = caller(hello_world)
# x()  # равносильно caller(hello_world)()


#########################################################################

# def summator(a, b):
#     return a + b
#
#
# def trace_decorator(some_func):
#     def new_func(a, b):
#         print(f'вызов {some_func} c аргументами {a} и {b}')
#         result = some_func(a, b)
#         print(f'вернули результат {result}')
#         return result
#
#     return new_func
#
#
# summator = trace_decorator(summator)
# six = summator(2, 4)
# two = summator(1, 1)
# пробела такой функции , что работает только с двумя аргументами
# заменим позиционными и именованными аргументами


def trace_decorator(some_func):
    def new_func(*args, **kwargs):
        print(f'вызов {some_func} c аргументами {args} и {kwargs}')
        result = some_func(*args, **kwargs)
        print(f'вернули результат {result}')
        return result

    return new_func


@trace_decorator  # равносильно summator = trace_decorator(summator)
def summator(a, b):
    return a + b


@trace_decorator  # можно импортировать из модуля
def multiply(a, b, c):
    return a * b * c


six = summator(2, 4)
two = summator(1, 1)
multiply(3, 2, 2)
