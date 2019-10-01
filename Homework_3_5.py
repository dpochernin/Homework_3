# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом (любым), то должна выполняться конкатенация,
# т. е. соединение, строк. В остальных случаях введённые числа суммируются.
s1 = input('Enter first string')
s2 = input('Enter second string')
try:
    s1 = float(s1)
    s2 = float(s2)
    print('Sum s1+s2:', s1 + s2)
except ValueError:
    print('Concatenation s1+s2', str(s1) + str(s2))
    