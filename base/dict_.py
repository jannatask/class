'========================Словари==========================='
# dict - изменяемый итеруемый неупорядочный(псевдопорядок), неиндексируемый тип данных, для хранения данных в парах {ключ:значение}

user = {'name': 'anonym', 'age':30, 'last name':'[Makers]'}
print(user['name']) #Anonym
print(user['age']) #age
print(user['last_name']) #makers

# ключами в словаре могут бфть только неизменяемыетипы данных
# ключи в слоарях должны быть уникальными

# '=====================Создание словарей============================'
# dict_ = {'a':1, 'b':2}
# # dict_ = ([('a':1),('b',2)])
# print(dict_)
# dict_ = (['a1','b2', 'c3'])
# print(dict_)   # {'a':'1', 'b':'2', 'c':'3'}

# dict_ = {}
# print(dict_['name'])
# dict_['age'] = 'makers'
# dict_['last_name'] = 'bootcamp'
# print(dict_)

'====================Методы словаря================'

'get - метод ,который получает значение по ключу, если указанного ключа нет , то выходит None -по умолчанию, мы можм его поменять'

user = {'name':'Anonym', 
        'age':15, 
        'last_name':'Makers'}
# print(user['id']) # error - KeyError
# print(user.get('id')) # None
# print(user.get('id', 'Такого ключа нет')) # такого ключа нет

# 'pop - удвляет пару по ключу и возвращает значение'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.pop('b')
# print(dict_) # {'a':1,'c':3}
# print(popped)  # 2       



'popitem - удаляет последнюю пару и возвращает ее'

# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_) #{'a':1, 'b':2}
# print(popped) # ('c',3)


'update -расширяет словарь парами из второго словаря'
# dict_1 = {1:'a',2:'a'}
# dict_2 = {2:'b', 3:'b'}
# dict_1.update(dict_2)
# print(dict_1) # {1:'a', 2:'b', 3:'b'}


# 'clear- очищает словарь'
# dict_ = {'a':1, 'b':2, 'c':3}
# dict_.clear()
# print(dict_) # {}


'fromkeys - для создания нового словаря, используя список ключей'

# dict_ = dict.fromkeys('hi')
# print(dict_) # {'h':None, 'i':None}
# dict_2 = dict.fromkeys(['hi', 123, True], 0)
# print(dict_2) # {'hi':0, 123:0, True:0}

'keys, values, items'
# keys =метод который возвращает все ключи
# values - метод, который возвращает все значения
# items - метод коиорый возвращает пары ключ и значение  виде tuple

# users = {
#     'name': 'Anonym',
#     'age':15,
#     'last_name': 'Makers'
# }
# print(users.keys())   # dict_keys(['name', 'age', 'last_name'])
# print(users.values()) # dict_keys
# print(users.items())


# '====================Итеерирование словарей========================'
# users = {
#     'name': 'Anonym',
#     'age':15,
#     'last_name': 'Makers'
# }

# for i in user:    # при итерации словаря будут приходить ключи
#     print(key)

# for value in user.values:
#     print(dict)
#     # при итерации словаря с методом  values (), приходят значения

# for item in user.items():
#     print(item)
# при итерации словаря с мптодом itens(),приходят tuple с ключем и значением
    

'------------------------------------------------------------'
# у вас есть dict_1 = {1:'a', 2:'b'}
# вам нужно создать новый словарь dict_2 при помощи кода
# {'a':1, 'b':2}

# dict_1 = {1:'a', 2:'b'}
# dict_2 = {}

# for k, v in dict_1.items()
#      dict_2[v] = k
#      print(dict_2)








