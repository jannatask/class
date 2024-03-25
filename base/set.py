'=======================Set======================'
#множества - изменяемый, неупорядоченный, итерируемый тип данных, предназначенный для хранения уникальных значений.
Множества могут хранить в себе только неизменяемый тип данных.Если внутри set, используете tuple, то и внутри turl'a должны быть незменяемые типы данных
({1, 2, 2, 23,('str', 12, True)}).В set работает правило - FIFO (first in first out)

# set_1 = {1, 0, True, 'hi'} # 1
# set_2 = {True, 0, 1, 'hi'} # True
# print(set_1, set_2)

'=======================FIFO/LIFO=================='
#  FIFO - first in first out   (очередь в банк, выйдет первым тот кто первым встал в очередь)
#  LIFO - last in first out    (стопка бумаг, выйдет та бумага которую вы поставили последним)



'==========================Методы set=================='
' add - добавляет элементы в set'
# set_1 = {1, 2, 3}
# set1.add(3) # {1, 2, 3} ничего не изменится 
# set1.add(5) # {1, 2, 3, 5}
# print(set1) # {1, 2, 3, 5}

'pop -удаляет случайный элемент из set(FIFO)'
# set2 = {1, 2, 3}
# popped = set2.pop()
# print(set2)


'remove - удаляет элемент из seta по значению'
# set3 = {1, 2, 3}
# set3.remove(3)
# print(set3)


print(dir(set))

'union - обединяет set1 и set2'

# set1 = {1,2,3}
# set2 = {4,5,6}
# set1.union(set2)
# print(set1)


'update - обединяет set1 и set2 и сохраняет изменения в set1'

# set1 = {1,2,3}
# set2 = {4,5,6}
# set1.update(set2)
# print(set1)


'difference (-) - на=ходит разницу из set1 при помощи set2'

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.differece(set2)) # {1,2}
# print(set2.differece(set1)) # {4,5}
# print(set1 - set2) # {1,2}
# print(set2 - set1) # {4,5}


'symmetric_differece - находит разницу '
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.symmetric_differece(set2))  # {1,2,4,5}


'intesection (&) - находит схожие элементы из двух сетов set1, set2'

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1.intersection(set2)) # {3,4}
# print(set1 & set2) # {3,4}
# print(set1)