"""
name = "Пользователь"
print(f"Добрый день, {name}.")
print("Привет, {}!".format(name))

#Список победителей
first_name = "Петя"
second_name = "Вася"
third_name = "Толя"
first_speed = float(input())
second_speed = float(input())
third_speed = float(input())
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name
print('1.' + first_name, '2.' + second_name, '3.' + third_name, sep="\n")


#Сила прокрастинации
year = float(input())
if year % 4 == 0  and year % 100 != 0  or  year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
  print("YES")
else:
  print("NO")

#А роза упала на лапу Азора
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
if a == d and b == c:
  print("YES")
else:
  print("NO") 

#Первому игроку приготовиться 
n1 = input()
n2 = input()
n3 = input()
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1
print(n1)

#Лучшая защита — шифрование
num = int(input())
s = num // 100
d = (num // 10) % 10
e = num % 10
n1 = d + e
n2 = s + d
if n1 > n2:
    print(n1, n2, sep="")
else:
    print(n2, n1, sep="")

#Красота спасёт мир    
num = int(input())
s = num // 100
d = (num // 10) % 10
e = num % 10
if d > s: 
    d, s = s, d
if e > d:
    e, d = d, e
if d > s: 
    d, s = s, d
if (e + s) == d * 2:
    print("YES")
else:
    print("NO")

#Властелин Чисел: Братство общей цифры    
e = int(input())
g = int(input())
p = int(input())
if e // 10 == g // 10 and g // 10 == p // 10:
    print(e // 10)
else:
    print(e % 10)

#Властелин Чисел: Две Башни   
num = int(input())
s = num // 100
d = (num // 10) % 10
e = num % 10
n1 = e * 10 + d
n2 = e * 10 + s
n3 = int(str(d) + str(e))
n4 = int(str(d) + str(s))
n5 = int(str(s) + str(e))
n6 = int(str(s) + str(d))
min_num = 100  # начальное большое значение
if n1 >= 10 and n1 < min_num:
    min_num = n1
if n2 >= 10 and n2 < min_num:
    min_num = n2
if n3 >= 10 and n3 < min_num:
    min_num = n3
if n4 >= 10 and n4 < min_num:
    min_num = n4
if n5 >= 10 and n5 < min_num:
    min_num = n5
if n6 >= 10 and n6 < min_num:
    min_num = n6
# Находим максимальное число
max_num = 0
if n1 > max_num:
    max_num = n1
if n2 > max_num:
    max_num = n2
if n3 > max_num:
    max_num = n3
if n4 > max_num:
    max_num = n4
if n5 > max_num:
    max_num = n5
if n6 > max_num:
    max_num = n6
print(min_num, max_num)


#Властелин Чисел: Возвращение Цезаря
one = int(input())
two = int(input())
one_one = one // 10
one_two = one % 10
two_one = two // 10
two_two = two % 10
max_num = max(one_one, one_two, two_one, two_two)
min_num = min(one_one, one_two, two_one, two_two)
sum = one_one + one_two + two_one + two_two
rem_f = sum - (max_num + min_num)
if rem_f > 9:
    rem = rem_f % 10
    print(f'{max_num}{rem}{min_num}')
else:
    print(f'{max_num}{rem_f}{min_num}')

#Легенды велогонок возвращаются: кто быстрее?
one = 'Петя'
two = 'Вася'
three = 'Толя'
o_speed = int(input())
two_speed = int(input())
three_speed = int(input())
if two_speed < three_speed:
    two_speed, three_speed = three_speed, two_speed
    two, three = three, two
if o_speed < two_speed:
    o_speed, two_speed = two_speed, o_speed
    one, two = two, one
if two_speed < three_speed:
    two_speed, three_speed = three_speed, two_speed
    two, three = three, two
print(f'{one:^24}')
print(f'{two:^8}')
print(f'{three:^40}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')


#Корень зла
a = float(input())
b = float(input())
c = float(input())


def f(a, b, c):
    if a == b == c == 0:
        return 'Infinite solutions'
    elif a == 0 and b != 0 and c != 0:
        return f'{-(c / b):.2f}'
    elif a == b == 0:
        return 'No solution'
    elif a == c == 0:
        return '0'
    else:
        disc = (b ** 2) - (4 * a * c)
        if disc == 0:
            return f'{(-b) / (2 * a):.2f}'
        elif disc > 0:
            x1 = (-b - (disc ** 0.5)) / (2 * a)
            x2 = (-b + (disc ** 0.5)) / (2 * a)
            return f'{min(x1, x2):.2f} {max(x1, x2):.2f}'
        else:
            return 'No solution'


print(f(a, b, c))



#Территория зла
a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c) ** 2 * 2
other = a ** 2 + b ** 2 + c ** 2

if maximum == other:
    print('100%')
elif maximum > other:
    print('велика')
else:
    print('крайне мала')


#Автоматизация безопасности
x = float(input())
y = float(input()) 
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 0 <= y <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 0 <= y <= 5 and (5 * x - 3 * y) > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif (0.25 * x ** 2 + 0.5 * x - 9) <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')

    
"""
#Зайка — 2
nature1 = input()
nature2 = input()
nature3 = input()
if nature1 > nature2:
    nature1, nature2 = nature2, nature1
if nature1 > nature3:
    nature1, nature3 = nature3, nature1
if nature2 > nature3:
    nature2, nature3 = nature3, nature2

if 'зайка' in nature1:
    print(nature1, len(nature1))
elif 'зайка' in nature2:
    print(nature2, len(nature2))
elif 'зайка' in nature3:
    print(nature3, len(nature3))