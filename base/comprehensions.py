'=======================Comprehensions======================='
# генератор ,с помощью которого можно создать последовательность используя цикл for в одну строку

# range()
# []
# {}
# {:}

# результат for элемент in последовательность 
gen = ('hi' for x in [23, 0, ])
print(gen)  # <generator object <genexpr> at 0x

'Создайте список состоящий из четких чисел 1 до 10 используя comprehensions'

list_ = []
for i in range(1,11):
    if i % 2 == 0:
        list_.append(i)
    else:
        list_.append(i)
print(list_)

list_ = [i if i % 2 == 0 else i*2 for i in range(1,11)] 
print(ist_) #['нечетный'. 'четный', 'нечетный']

'В comprehension можно добавлять условия,там их бывает 2 вида'
'1 - тернарный оператор,пишется перед циклом,так как используем и if , и else'
'2 - фильтр пишется после цикла, так как используется только if'

# создать спимок из существующего списка,оставив только строки 
# list_1 = [12, True, None, 'hi', 0 , False, 'makers', 'world']

# list_2 = [i for i in list_1 if type(i) == str]
# print(list_2) # ['hi', 'makers','world']

# a = 12
# prin(type(a)==int)  #True


'============================Виды comprehension=========================='
'1 - list comprehension'
'2 - dict comprehension'
'3 - set comprehension'

'Dict comprehension'
dict_1 = {i:i for i in range(1, 11)}
print(dict_1) # (1:1, 2:4, 3:9, ...)
# (1:1, 2:4, 3:9, ...)

'Дан словарь , поменяйте ключи и значения с помощью comprehension'
dict_1 = {'a':1, 'b':2, 'c':3} 
dict_2 = {value:key for key, value in dict_1.items()} # {1:'a', 2:'b', 3:'c'}
print(dict_2)



'Дан словарь где значения - списки из чисел, создайте словарь , где значения будут суммы этих списков '

dict_1 = {
    'a':[1,2,3],
    'b':[12,0,1],
    'c':[32,0,0,10]
    }
dict_2 = {k:sum(v) for k,v in dict_1.items()}
# {'a':6, 'b':13, 'c':42}

'Set comprehension'

set_1 = {i for i in range(1,11)}
print(set_1) #{1,2,3,4,5,6,7,8,9,10}

set_1 = {2, 3, 4, 15,1}
set_2 = {i**2 for i in set_1}  # {4,9,16, }
print(set_2)


set_1 = {12, 4, 34, 5, 6}
set_2 = {str(i) for i in set_1}  # {'12','4','34','5','6'}
print(set_2)



'Сохраните только строки'
# set_1 = {1, 12, 'hi', 34, True, 'makers'}
# set_2 = {i for i in set_1 if type(i) == str} # {'hi', 'makers'}


'Сохраните только строки, те строки в которых хранятся числа переведите с  int "12" -> 12, а простые строки с символами и буквами сохраните 

# set_1 = {12, True, 'HI', 23, '10' 'makers', False, '1'}
# set_2 = {int(i) if i.isdigit() else i for i in set_1 if type(i)==str}

# # {'HI', '10', 'makers', '1'}


'Создайте словарь , где ключи будут числа от 1 до 5, а значениями  - списки с числами от 1 до жтого числа'

{
  1:[1],
  2:[1,2],
  3:[1,2,3],
  4:[1,2,3,4],
  5:[1,2,3,4,5]
}

dict_1 = {i: [i for i in range(1,i+1)] for i in range(1,6)}
print(dict_1)