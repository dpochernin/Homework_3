# Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
import math

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
print('From list')
while l:
    print(l.pop(i))

# ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и «удаляет» первый символ строки,
# пока она не станет пустой?
s = '0123456789'
print('From string')
while s:
    print(s[0])
    s = s[1:]

# Напишите цикл, который выводит на экран и удаляет элементы списка
# от самого маленького до самого большого, пока он не останется пустым.
l = [2, 1, 2, 4, 1, 5, 6, 7, 8, 9]
l1 = l.copy()
# метод просто с сортировкой и попом - выводит значения несколько раз в случае их дублей
l.sort()
print("With multiple values (")
while l:
    print(l.pop())

# метод с попом старшего элемента и поиском его дублей и тихим их удалением
l1.sort()
print("Without multiple values")
while l1:
    k = l1.pop()
    while True:
        try: l1.remove(k)
        except ValueError: break
    print(k)

# ** Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
l = [1, 1, 2, 2, 4, 1, 1, 1, 5, 6, 7, 8, 9, 0]
#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i, k, s, v = 0, 0, 0, 0
while l[i] != 0:
    if l[i] == l[i+1]:
        k += 1
    elif k > s:
        s = k
        k = 0  # забыл обнуление счетчика совпадений
        v = l[i]
    i += 1
if s == 0: print('No mach in raw elements are in list')  # добавлена проверка если одинаковых значений подряд
else: print('Element ', v, 'is ', s, 'times in this mas')
