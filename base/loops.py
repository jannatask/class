'=====================Циклы====================='
# цикл -это канструкция ,который повторяеткод несколько раз
# есть 2 вида цикла
'1. for -цикл, который работает с итеруемым обьектои. Цикл заканчивает работу, когда доходит по последнего элемента итеруемого обьекта'

'2. while - цикл, который  работает до тех пор пока условии верное(True) '

' Итеруемый обьект - это какая то последовательность , например: [1, 23, "hi"],"makers", (123, True, 1,5), dict, set'

'Итерация - процесс перебоя итеруемого обьекта(когда мы по очереди вытаскиваем элементы в последоватешльности)'

'----------------------------------------------------'
'FOR'

# list_ = [12, 'hi', True, None, [0,0,0]]

# for element in list_:
#     print(element)

for letter in 'hello world':
    print(letter)

# h
# e
# l
# l
# o
# 
# w
# o
# r
# l
# d

for number in [12, 3, 4, 0, -1, 20]:
    print(number * 2)

# 24
#  6
# 8
# 0
# -2
# 40

# list_ = [2, 12, 5, 3]
# for i in list_:
#      print(i ** 2)

'------------------------------------'
# text = 'makers'
# for a in text:
#     print(a)

# '------------------------------------'

# list_ = [2, 5, 20, 10, 9, -1]
# # нужно распечатать только четные числа

# for i in list_:
#     if i % 2 == 0:
#         print(i)

# 20
# 10
# 2


'WHILE'

#  n = 1
# while n < 10:
#     print('hello world')
#     n = n + 1

# n = 0
# while n < 10:
#     print('hi')
#     n += 1n


# останавливает ваш код в терминале
ctrl + c
ctrl + z


'===============================Ключевые слова в циклах========================'
# break -принудительная остановка цикла
# continue -пропускает итерацию, продолжает со следующей итерации

# range() # генератор (создание)

# for i in range(1, 11)
#     if i == 3:
#         continue
#     print(i)

# распечатает кроме 3
    
# for i in range(11)
#     if i == 2:
#         break
#     print(i)

# n = 1
# while n <= 10:
#     n = n + 1
#     if n == 2:
#           continue
#     print(n)

# 3
# 4
...
# 10



# n = 0
# while n < 10:
#     print(n)
#     if n > 5
#     break
#     n += 1
 #распечатает от 0 до 6

















    










