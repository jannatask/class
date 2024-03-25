
# `````````````````String``````````````````
# строки - неизменяемый тип данных,который предназначен для хранения текста, заключенного в одинарные либо двойные кавычки

string1 = ' строка с одинарными кавычками '
string2 = 'строка с двойными кавычками'
string3 = "Don't" # внутри двойных кавычек все одинарнае кавычки просто часть текста
string4 = 'название  магазина "Азбука"'
string5 = '''
Многострочный текст 
в одинарных кавычках
Тут можно использовать и одинарный и двойные кавычки
'''

string6 = """ 
Многострочный текст 
в двойных кавычках
Тут можно использовать и одинарные и двойнве кавычки
"""
string7 ='hello' + ' ' 'world' #hello world
print(string7) 

string8 = 'A' * 10 # AAAAAAAAAA
print(string8)


# ===============================Экранизация строк=======================
'\n' #перенос на новую строку
print('hello world') #hello world
print('hello\nwworld') # hello 
                       #world
#  -------------------------------------------
print('he\nllo world') # he
                       #llo world
'----------------------------------------'

'\t' #табуляция(несколько пробелов)
print('hello\twworld') #hello     world
print('he\tllo world') #he     llo world

'\v'  # перенос на новую строку со смещением вправо на длину предыдущей строки
print('hello\vworld\vmakers') #hello
                               #      world
                                 #         makers
'\r' #перенос каретки в самое начало строки 
print('helloworld\rMa') # Mallo world

'\''  #jотображение  ' 
"\"" #отображение "

print('Don\'t') # Don't

'\\' #отображение  \
print('команда \\n - переносит строку')



# =========================Форматирование строк==========================
title = 'Iphone 15'
price = 1000
print('Я купил title за price $')

shop = 'Makers'
'1. f-строка'
#  print(f'Я купил {title} за {price} $, в магазине {shop}')

'2. %s'
print('Я купил %s за %s$, в магазине %s' % (price, title, shop))


'3. str.format'
print('Я купил {} за {}$, в магазине {}'.format(title, price , shop))


# ==============================Методы строк (str)========================

# метолы - функции, которые относятся к определенному типу данных(классу), к ним мы обращаемся через точку

print(dir(str))


# string = 'hello world'

# print(string.upper()) #HELLO WORLD
# print(string.lower()) #hello world
# print(string.swapcase()) #hello WORLD

# print(string.title()) # Hello World
# print(string.capitalize()) # Hello world


# print(string.islower()) #True
# print(string.isupper()) #False

# print(string.center(12, '*')) # '*****Hi*****'

# string = 'hello world'
# print(string.count('l')) # 3
# print(string.count('el')) # 1
# print(string.count('o w')) # 1
# print(string.count('hello')) # 1

# print(string.startwith('h')) #True
# print(string.startwith('H')) #False
# print(string.startwith('hello')) #True
# print(string.endswith('ld')) #True

string = 'makers'
print(string.isalpha) #True, проверяет на буквы
print(string.isdigit()) # False, проверяет на числа
print(string.isalnum()) #True ,проверяет является ли строка числом или буквой тлт и числом и буквойбесли есть символ то вернет False
string = 'hello world makers bootcamp'
print(string.split('o')) #['hello, 'world', 'makers', 'bootcamp']
# ['hell', ' w', 'rld makers b', '', 'tcamp']

print(string.replace('','$'))
string = '$12 hi$$$$$$$$$$'
print(string.strip('$'))

# '' .join(string) #string это переменное которая хранит типданных list[]

===========================Индексы=============================
# инжекс - порядковый номпер элемента в последовательности(индекс начинается с 0)

#-11-10-9-8-7-6-5-4-3-2-1
# 'h e l l o o  w o r l d[']
#  0 1 2 3 4 5 6 7 8 9 10

# string ='hello world'
# print(string[0]) # 'h'
# print(string[-1]) #'d'
# print(string[5]) #' '

# # срез [start:end(не включительно)step]
# string[6:10] #worl
# string[:5] # hello
# print(string[::2]) #hlowrd
# print(string[::-1]) #dlrow olleh
# print(string[::-2]) #drwolf

