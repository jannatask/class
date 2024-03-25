'==========================List=========================='
# списки - изменямые ,индексируемый,упорядоченны1,итерируемый тип данных,предназначенный для хранения любых данных в определеенном порядке

list_1 = [1, 2, 14, 'hello' , True, [0,0,0], None]
         # 0 1  2      3        4      5       6

list_1[3] # 'hello'
list_1[-1] # None
list_1[-2][-1]  # 0
list_1[3][-2] # l
list_1[5] # [0,0,0]

'range(start, end( не включительно), step) -это функция генератор ,которая генерирует\создает диапазон от start до end(не включительно)'
#list('hello') -> ['h','e','l','l','o']
list_2 = list(range(0, 101)) # [0,1,1....99,100]
print(list_2)
print(list(range(50,70))) # [50,51,....,69,70]

print(list(range(0, 11, 2)))
# [0, 2, 4, 6, 10] шаг 2
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #шаг1
# [0, 3, 6,9] шаг 3
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,0] шаг -1


'=========================Методы списков============================'
'append -добавление элемента конец списка '

list_ = []
list_.append(1)
list_.append('hello world')
list_.append(True)
print(list_) # [1, 'hello world', True]

'pop -удаление элемента тз списка по индексу, возвращает удаленный элемент. Если не ууказать индекс,то удалит с конца'


# list_ = [90,True, None, 'Hi']
# popped = list_.pop(1)
# print(list_) # [90, None, 'Hi']
# print(popped) #True

'remove -это удаление элемента из списка по значению'

# list_ = [1, 2, 3. 5. 99 , 0, -11]
# list_.remove(5)
# print(list_)

'count -считает кол-во принятого элемента в списке'

# list_ = [1, 23, 1 , 4, 5, 6, 'hi', 1, 'hi', 1, 7, 1,8, 1, 'Hi']
# print(list_.count(1)) # 5
# print(list_.count(7)) # 2
# print(list_.count('hi')) # 2

'index - возвращает индекс первого вхождения принятого элемента'

list_= ['hi', 1, 341, 2, 0, 2, 1, 99, 10]
print(list_.index('hi')) # 0

'extend -расшттряет список при поиощи другого списка'

list_1 = [1,2,3]
list_2 = [0,0,0]
list_1.append(list_22) # [1,2,3,[0,0,0]]
print(list_1)
list_1.extend(list_2)  # [1,2,3,0,0,0]
print(list_1)

'reverse -изменяет список ,расставляя его элементы в обратном порядке'

list_ = ['hi', 1, 2, 3, True, [1,2,3]]
list_.reverse()
print(list_) # [[1,2,3], True, 3,2, 1, 'hi']

'sort- сортирует список, состоящий из элементов одно типа данных'

list_ = [12, 4, 1, 0, 25, 7]
list_.sort()
print(list_) # [0, 1, 4, 7, 12, 25]

list_= ['a', 'b', 'c', 'A', 'B']
list_.sort()
print(list_) # ['A', 'B','a', 'b', 'c']


'clear -очищает список'
list_ = [12, 42, 1, 'hi', 0, False, None]
list_.clear()
print(list_) # []

len([12, 4, 5, [1,2,3]]) # 4

# a = 10
# b = 5
# c = 2
# a, b, c = 10, 5, 4
# print(a, b, c)


# meshok = ['kartoshka', 'luk', 'luk', 'kartoshka', 'luk']

# paket1 = []
# paket2 = []
# for ruka in meshok:
#     if ruka == 'kartoshka':
#         paket1.append(ruka)
#     elif ruka == "luk":
#         paket2.append(ruka)

#         print(paket1)
#         print(paket2)















