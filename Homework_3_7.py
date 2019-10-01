import string

s = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
"""
# Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
words = s.splitlines()
print(words)
for word in range(len(words)):
    words.extend(words[0].strip().split(' '))
    words.remove(words[0])
    print(words)
print('in text are ', len(words), 'words')

# Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)
for word in range(len(words)):
    for char in [punct for punct in string.punctuation]:
        words[word] = (words[word].strip(char))
print(words)

# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
words.sort()
print(words)

# Посчитать, сколько раз встречается каждое слово
# Слова с большой буквы и с маленькой это все равно одно и тоже слово
dict_words = {word.lower(): 0 for word in words}
for word in words:
    for k in dict_words.keys():
        if word.lower() == k: dict_words[k] += 1
print(dict_words)
