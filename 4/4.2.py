"""
#Генератор списков
def make_list(length, value=0):
    return [value for _ in range(length)]
print(make_list(5))


#Генератор матриц

def make_matrix(size, value=0):
    if isinstance(size, tuple):
        n, m = size
    else:
        n = m = size
    return [[value for _ in range(n)] for _ in range(m)]
"""
#Функциональный нод 2.0
def gcd(*args):
    a = args[0]
    for b in args[1:]:
        while b:
            a, b = b, a % b
    return a


print(gcd(3, 102, 39, 768))