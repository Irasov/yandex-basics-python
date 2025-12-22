"""
sum = 0
while price := float(input()):
    if price >= 500:
        price = price * 0.9
    sum = sum + price
print(sum)

#НОД и НОК
a = int(input())
b = int(input())
aa = a
bb = b
while b:
    a, b = b, a % b
    print(a)
    print(b)
print(a)
print(int((aa * bb) / a)) 

#repeat
text = input()
for _ in range(int(input())):
    print(text)

#факториал
res = 1
for n in range(2, int(input()) + 1):
    res *= n
print(res)


#Маршрут построен
x = 0
y = 0
while (dir := input()) != 'СТОП':
    move = int(input())
    match dir:
        case 'СЕВЕР':
            x += move
        case 'ЮГ':
            x -= move
        case 'ВОСТОК':
            y += move
        case 'ЗАПАД':
            y -= move
print(x)
print(y)


#Цифровая сумма
num = int(input())
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print(sum)


#Зайка4
count = 0
for _ in range(int(input())):
    text = input()
    if 'Зайка' in text:
        count += 1
print(count)


#А роза упала на лапу Азора 2.0
num = int(input())
orig = num
revers = 0
while num > 0:
    dig = num % 10
    revers = revers * 10 + dig
    num //= 10
if orig == revers:
    print('YES')
else:
    print('NO')


#Чётная чистота
num = int(input())
res = 0
pow = 1
while num > 0:
    if num % 2 != 0:
        res += (num % 10) * pow
        pow *= 10
    num //= 10
print(res)


#Простая задача2.0
number = int(input())
divisor = 1

if number < 2:
    print(number)
while number > 1:
    divisor += 1
    if not number % divisor:
        print(divisor, end='')
        if number != divisor:
            print(' *', end=' ')
        number //= divisor
        divisor = 1


#Игра в «Угадайку»
number = 500
delta = number // 2
print(number)

while (answer := input()) != 'Угадал!':
    if answer == 'Меньше':
        number = number - delta
    if answer == 'Больше':
        number = number + delta
    if delta >= 2:
        delta = (delta + 1) // 2
    print(number)


"""
#Хайпанём немножечко!
