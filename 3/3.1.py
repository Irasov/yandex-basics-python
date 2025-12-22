"""
#Кручу-верчу
str = input()
for letter in str:
    print(letter)


#Анонс новости
res = ''
length = int(input())
for _ in range(int(input())):
    str = input()
    if len(str) > length:
        res += str[:length - 3] + '...\n'
    else:
        res += str + '\n'
print(res)


#Очистка данных
str = input()
res = ""
while str != "":
    if str[:2] == '##' and str[-3:] != '@@@':
        res += str[2:] + '\n'
    elif str[-3:] != '@@@':
        res += str + '\n'
    str = input()
print(res)


#А роза упала на лапу Азора 4.0
str = input()
if str == str[::-1]:
    print('YES')
else: 
    print('NO')



#Зайка — 6
count = 0
for _ in range(int(input())):
    count += input().count('зайка')
print(count)


#А и Б сидели на трубе
a, b = input().split()
print(int(a) + int(b))


#Зайка — 7
res = ""
for _ in range(int(input())):
    st = input()
    if st.find('зайка') != -1:
        res += str(st.find('зайка') + 1) + '\n'
    else: 
        res += 'Заек нет =(\n'
print(res)



#Без комментариев
res = ''
text = input()
while text != '':
    if text.startswith('#'): 
        pass
    elif text.find('#') != -1 and text.find('#') != 0:
        res += text[:text.find('#')].rstrip() + '\n'
    else: 
        res += text.rstrip() + '\n'
    text = input()
print(res)


#Частотный анализ на минималках
letters = []
counts = []
text = input()
res = ""
while text != 'ФИНИШ':
    res += text
    text = input()
res = res.replace(' ', '').lower()
for letter in res:
    if (letter in letters):
        if (index := letters.index(letter)) != -1:
            counts[index] += 1
    else:
        letters.append(letter)
        counts.append(1)
maxx = 0
max_letters = []
for i, num in enumerate(counts):
    if num > maxx:
        maxx = num
        max_letters = [letters[i]]
    elif num == max:
        max_letters.append(letters[i])
max_letters.sort()
print(max_letters[0])



#Найдётся всё
count = int(input())
heads = []
find_heads = []
for _ in range(count):
    text = input()
    heads.append(text)
find_head = input().lower()
for head in heads:
    if find_head in head.lower():
        find_heads.append(head)
for head in find_heads:
    print(head)


#Меню питания
menu = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
index = -1
for _ in range(int(input())):
    if index < len(menu):
        index += 1
    if index >= len(menu):
        index = 0
    print(menu[index])



#Массовое возведение в степень
count = int(input())
numbers = []
for _ in range(count):
    numbers.append(int(input()))
deg = int(input())
for number in numbers:
    print(number ** deg)


#Массовое возведение в степень 2.0
numbers = input().split()
deg = int(input())
degs = []
for num in numbers:
    degs.append(str(int(num) ** deg))
print(' '.join(degs))


"""
#НОД 3.0
numbers = input().split()
a = 0
b = 0
for num in numbers:
    if a == 0:
        a = int(num)
    elif b == 0:
        b = int(num)
        while b:
            a, b = b, a % b
print(a)