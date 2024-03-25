'==========================Декораторы==================='
# функция высшего порядка - функция , которая принимает в аргументы другуую функцию,
# вызывает внутри функцию и возвращает функцию

def func():
    ...


def func2(): # функция высшего порядка, так как принимает другую функцию в аргументы
    a()

func2(func1)

# Декораторы - это функция высшего поряка, которая нужна чтобы расширить функционал другой функции
не изменяя ее (функция обертка)

# def glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         return text + 'тихо'
#     return wrapper

# def gun():
#     return 'Стреляет'

# wrapper = glushitel(gun)
# result = a()
# print(result)
# print(gun())

# def glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         return text + 'тихо'
#     return wrapper

# @glushitel
# def gun():
#      return 'Стреляет'

# result = gun()

# from datetime import datetime

# def func_start_time(func):
#     def wrapper():
#         time = datetime.now().strftime('%d.%m.%Y %H:%M')
#         print(f'Наша функция запустилась {time_}')
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('hi')

# @func_start_time
# def func1():
#     print('hello')

# func()
# func1()



