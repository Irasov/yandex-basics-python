"""
#Список квадратов
[x ** 2 for x in range(a, b + 1)]


#Список квадратов2
[x ** 2 for x in range(a, b + (1 if a < b else -1), 1 if a < b else -1)]

#Основы фильтрации
a = 1
b = 5
d = 2
print(a % d)
list = [x for x in range(a + (d - a % d) % d,  b + 1, d)]
print(list)


#Множество нечетных чисел
numbers = [1, 2, 3, 4, 5]
res = set([number for number in numbers if number % 2 != 0])
print(res)



#Множество всех полных квадратов
numbers = [1, 2, 3, 4, 5]
res = {num for num in numbers if num == int(num ** 0.5) ** 2}
print(res)


#Длины всех слов
sentence = 'mama mila ramu'
res = [len(word) for word in sentence.split(' ')]
print(res)


#Цифровая выжимка
text = '33 коровы,\n' + \
    '33 коровы,\n' + \
    '33 коровы -\n' + \
    'Свежая строка.\n' + \
    '33 коровы,\n' + \
    'Стих родился новый,\n' + \
    'Как стакан парного молока.\n' + \
    'Стих родился новый,\n' + \
    'Как стакан парного молока.\n'
res = ''.join(num for num in text if num in '0123456789')
print(res)



#Аббревиатура
string = 'Российская Федерация'
res = ''.join(word[0].upper() for word in string.split())
print(res)


#Преобразование в строку
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
res = ' - '.join(str(num) for num in sorted({j for j in numbers}))
print(res)



#Огласите список
words = 'Ехали медведи на велосипеде'
res = [
    word
    for word in words.split()
    if sum(1 for letter in word.lower() if letter in "аяуюоёэеиы" or letter in "aeiouy")
    >= 3
]
print(res)


#Выявление уникальности
numbers = [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]
res = {num for num in numbers if numbers.count(num) == 1}
print(res)


"""
#Максимальное произведение
numbers = {1, 2, 3, 4, 5}
res = max(first * second for first in numbers for second in numbers if second != first)
print(res)