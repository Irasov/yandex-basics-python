"""

#Математика — круто, но это не точно
from math import log, cos, sin, pi, e
x = float(input())
a = log(x ** (3 / 16), 32)
b = x ** cos((pi * x) / (2 * e))
c = sin(x / pi) ** 2
print(a + b - c)


#Потоковый НОД
import sys
from math import gcd
for row in sys.stdin:
    res = gcd(*map(int, row.split()))
    print(res)


#Есть варианты?
from math import comb
n, m = map(int, input().split())
vas = comb(n - 1, m - 1)
sum = comb(n, m)
print(vas, sum)


#Среднее не арифметическое
from math import prod
nums = list(map(float, input().split()))
res = prod(nums) ** (1 / len(nums))
print(res)

"""
#Шаг навстречу
from math import cos, sin, dist
x, y = map(float, input().split())
ro, phi = map(float, input().split())
p_x = ro * cos(phi)
p_y = ro * sin(phi)
res = dist((x, y), (p_x, p_y))
print(res)

