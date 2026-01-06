"""
#Генератор списков
def make_list(length, value=0):
    return [value for _ in range(length)]
print(make_list(5))


"""
#Генератор матриц

def make_matrix(size, value=0):
    if isinstance(size, tuple):
        n, m = size
    else:
        n = m = size
    return [[value for _ in range(n)] for _ in range(m)]