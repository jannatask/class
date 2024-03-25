'===================Области видимости================'
# LEGB - local enclosed global build-in

'Building-in (Встроенное пространство)'
# Это пространство , которое находится в python (print, input, int, str, sum)

'Global(Глобальное пространство)'
# Это пространство , которое находится у вас в файле
# globals() - показывает все глобальные переменные

a = 5
b = 'hello'
print(globals())

'Enclosed(Замкнутое)'
# Это пространство которое находится во вложенных функциях, 

var = 'global'

def func():
    # локальное пространство для глобального пространства
    # замкнутое пространство (потому что более локальное пространство)
#     var = 'enclosed'
#     def func2():
#         # локальное пространство для пространствв func
#         var = 'local'
#      print(var)
#     print(var)
#     func2()

# print(var)
# func()
# # 1.enclosed local local
#2.global enclosed local

'Local(Локальное пространство)'
# Это пространство , которое находится внутри функции
# locals() - выводит переменные локального пространства

# a = 10

# def func(a, b):
#     print(a, b)
#     print('Глобальное', globals())
#     print('Локальное', locals())

# func(0, 1)


'global - это оператор который позволяет менять переменную с глобального пространства'


# var = 'global'
# def func():
#     var = 1

# func()
# print(var)
              



# def func():
#     var = 'enclosed'
#     def fuc2():
#         nonlocal var
#         var = 'local'
#     print(var) # enclosed
#     func2()
#     print(var) # local


# fuc()

'nonlocal - это оператор, который позволяет менять переменнуую с нелокального пространства'


# Напишите функцию которая увеличает глобальную переменную count
  
count = 0

def incr():
    global count 
    count = count + 1


incr() # 1
incr() # 2 
incr() # 3
incr() # 4
incr() # 5
print(count) # 5