'''
#Не таблица умножения заданного размера.
num = int(input()) + 1
for i in range(1, num):
    for j in range(1, num):
        print(f'{j} * {i} = {j * i}')


#Новогоднее настроение

count = int(input())
num = 1
row = 1
col = 1
while num <= count:
    while col <= row and num <= count:
        print(num, end=" ")
        col += 1
        num += 1
    col = 1
    row += 1
    print("")


#Суммарная сумма
sum = 0
for _ in range(int(input())):
    num = int(input())
    while num > 0:
        sum += num % 10
        num //= 10
print(sum)


#Зайка-5
sum = 0
for _ in range(int(input())):
    fl = True
    str = ''
    while str != 'ВСЁ':
        str = input()
        if str == 'зайка' and fl:
            sum += 1
            fl = False
print(sum)



#НОД 2.0
a = 0
b = 0
for _ in range(int(input())):
    if a == 0:
        a = int(input())
    else:
        b = int(input())
    if a and b:
        while b:
            a, b = b, a % b   
print(a)


#На старт! Внимание! Марш!
start = 3
player = 1
count = int(input())
for i in range(count):
    for j in range(start, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {player}!!!')
    player += 1
    start += 1



#Максимальная сумма
max = 0
max_name =''
num = 0
name = ''
for _ in range(int(input())):
    sum = 0
    name = input()
    num = int(input())
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)
    if sum >= max:
        max = sum
        max_name = name
print(max_name)


#Большое число
sum = 0
for _ in range(int(input())):
    n_max = 0
    n = int(input())
    while n > 0:
        if n % 10 > n_max:
            n_max = n % 10
        n //= 10
    sum = sum * 10 + n_max
print(sum)


'''
#Мы делили апельсин
count = int(input())
print('А Б В')
for a in range(1, count):
    for b in range(1, count):
        for c in range(1, count):
            if a + b + c == count:
                print(f'{a} {b} {c}')