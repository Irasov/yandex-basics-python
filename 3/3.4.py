'''
#Автоматизация списка
data = input().split()
for index, el in enumerate(data, 1):
    print(f'{index}. {el}')


#Сборы на прогулку
one_list = input().split(', ')
two_list = input().split(', ')
for one, two in zip(one_list, two_list):
    print(one, '-', two)


#Рациональная считалочка
from itertools import count
start, end, step = map(float, input().split())
for x in count(start, step):
    if x >= end:
        break
    print(x)s


#Словарная ёлка
from itertools import accumulate 
a = accumulate([word + ' ' for word in input().split()])
for x in a:
    print(x)


#Список покупок
from itertools import chain, accumulate
one_list = input().split(', ')
two_list = input().split(', ')
three_list = input().split(', ')

for index, el in enumerate(sorted(chain(one_list, two_list, three_list)),1):
    print(f'{index}. {el}')



#Колода карт
from itertools import product
suits = ['пик', 'треф', 'бубен', 'червей'] 
weights = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
excp = input()
deck = list(product(weights, suits))
for card in [card for card in deck if card[1] != excp]:
    print(card[0], card[1])

    

#Игровая сетка
from itertools import combinations
players = []
for _ in range(int(input())):
    players.append(input())
pairs = combinations(players, 2) 
for pair in pairs:
    print(f'{pair[0]} - {pair[1]}')


#Меню питания 2.0
from itertools import cycle, islice
porridge = [input() for _ in range(int(input()))]
n = int(input())
print('\n'.join(islice(cycle(porridge), n)))



#Таблица умножения 3.0
from itertools import product, islice
n = int(input())
table = [x * y for x,y in product(range(1, n + 1), repeat=2)]
for x in range(n):
    print(*islice(table, x * n, (x + 1) * n))



#Мы делили апельсин 2.0
from itertools import product
n = int(input())
table = list(product(range(1, n - 1), repeat=3))
print('А','Б','В')
for i in range(len(table)):
  if sum(table[i]) == n:
    print(*table[i])

'''   
#Числовой прямоугольник 3.0
n = int(input())
m = int(input())
numbers = [num for num in range(1, n * m + 1)]
iters = [iter(numbers)] * m
res = list(zip(*iters))
width = len(str(n * m))
for row in res:
    for x in row:
        print(f"{x:>{width}}", end=" ")
    print()
