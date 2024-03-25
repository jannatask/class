'==================Exceptions========================'
# Исключение - обьекты , которые прерывают работу кода,если не были обработаны

SyntaxError
# исключение , которое выходит, когда в коде допущена синтаксическая ошибка

'''
a = 
SyntaError
'''

NameError
# исключение , которое выходит , когла мы обращаемпя к несуществуещей переменной 

'''
num1 = 15
print(num5)
NameEroor
'''

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу

'''
list_ = [12, 20, 0, 2]
print(list_[1000])
IndexError
'''


'''
[12, 0, 24, 'hi'].pop(1000)
IndexError: pop index out of range
'''

'''
[].pop()
IndexErrror: pop from empty list
'''


KeyError
# исключение, которое выходит, когда мы обращаемся по несуществующему ключу

''' 
dict_ = {'a' :1}
dict_['c']
KeyError
'''


'''
dict_ = {'a' :1}
dict_.get('c')
ошибки не будет!!! Так ккакк get не вызывает ошибку, а вернет None, если такого ключа нет
'''

ValueError

# исключение выходит, когда мы передаем в функцию не корректный для нее тип данных
# когда мы распаковываем итеруемый обьект на несколько переменных и количество переменных не совпадает с кол-во элементов


'''
innt('10dfh')
ValueError
'''

'''
a, b = 1, 2, 3
ValueError
'''

TypeError
# Исключение выходит , когда мы пытаемся использовать методы не свойственные какому то типы данных
# когда мы пытаемсч передпть функции больше или меньше аргументов чеем принимает функция

'''
for i in 1235:
...
TypeError
'''

'''
"5" + 5
TypeError
'''

'''
{[1,2,3]}:'hi'
TypeError
'''

'''
input('Введите число', 123)
TypeError
'''


'''
[].append()
TypeError
'''

ZeroDivisionError
'''
45/0
ZeroDivisionError
'''

'''
45 // 0
ZeroDivisionError
'''

'''
45 % 0
ZeroDivisionEarror
'''


AttributeError
# выходит, когда мы обращаемся к несуществуещему аттрибуту или методу обьекта(типа данных)
'''[1,23,1,56].replace('a', '')
AtteributeError
'''

'''
'makers' . pop(0)
AttributeError
'''

IndentationError
# выходит ,когда мы не  правильно используем отступы

'''
  a = 5
IndentationError
'''

'''
for i in range(11):
print(i)
IndentationError
'''


Exception
# исключение ,которое создали , чтобы его вызывать


'======================Вызов исключений======================='
raise NameError('Просто вызывают NameError')
raise IndexError
raise KeyError


'=====================Обработка исключений====================='
# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обработывть вызванное исключение

# try: # код, который может вызвать ошибку\иссключение
#     num = innt(input('Введите число: '))
# except ValueError: # Ожидаемую исключение
#      # Обработку на исключение которой поймали 
#     print(' Вы ввели не число')
# else:  # код который отработает , ессли исключения не вышло
#     print(f'Вы ввели число {num}')
# finnaly:  # работает всегда
#     print('До свидание')
   
try :
    ...
    num = int(input('Введите число: '))
    res = 10 / num
except (ValuError, ZeroDivisionError):
    print('Что-то пошло не так')

# except: оброаботывает все исключения,котрые могут выйти
# except Exception: оброаботывает все исключения,которые могут выйти
    
# можем указать в except несколько исключений при помощи скобок и запятой except (ValueError,TypeErroor, ZeroDivisionError)
    

try:
    raise NameError
except NameError:
    print(1)


'Напишите программу при помощи try-except, пользователь вводит число , вам нужно сделать проверку на положительность и 0.'
'положительное число, должно выходить исключение ValueError'
'Отрицательное число, должно выходить иcключение TypeError'
'0, должно выходить исключение ZeroDivisionError'


# try:
#     num = int(input('Введите число'))
# if  num == 0:
#      raise ZeroDivisionEarror
# elif num > 0:
#     raise ValueError
# elif num < 0:
#     raise TypeError
# except ValueError:
#     print('Положительное')
# except TypeError:
#     print('Отрицательно')
# except ZeroDivisionError:
#     print('0')
