# Пишем функцию, которая попросит ввести число.
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число.
def input_float() -> float:
    while True:
        a = input('Enter digit')  # ну насколько я знаю делать функции которые требуют такой ввод в себя
        try:  # или из себя прям что-то печатают - это не есть гуд
            a = float(a)
        except ValueError:
            print('Value in not digit')
        else:
            return a
            break


# Пишем функцию, которая попросит пользователя ввести слово
# (строка без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово
def input_word() -> str:
    while True:
        a = input('Enter one word')
        if a.strip().find(' ') != -1:
            print('You enter not ONE word')
        else:
            return a
            break


# Написать функцию is_year_leap,
# принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(y: int) -> bool:
    try:
        if (y % 4) or (not (y % 100) and (y % 400)):
            return False
        else:
            return True
    except TypeError:
        print('ERROR', y, 'is not year')  # в условии не задано, но добавил что если не число, то выдает "ошибку"
        return False  # и возвращает False, или лучше None ?


# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.
def triangle_possible(a: float, b: float, c: float) -> bool:
    abc = [a, b, c]
    abc.sort()
    if (abc[0] + abc[1]) > abc[2]:
        return True
    else:
        return False


# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и если существует,
# то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний) или не треугольник (Not a triangle).
def triangle_type(a: float, b: float, c: float) -> str:
    if triangle_possible(a, b, c):
        if a == b and b == c:
            return 'Equilateral triangle'
        elif a == b or b ==c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else: return 'Not a triangle'


# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2-x1)**2+(y2-y1)**2)**0.5


l = []
for i in range(4):
    l.append(input_float())
print(distance(l[0], l[1], l[2], l[3]))
