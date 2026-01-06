
"""
#Функциональное приветствие
def print_hello(name):
    print(f"Hello, {name}!")


#Функциональный НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


#Длина числа

def number_length(n):
    return str(len(str(abs(n))))

    

#Копейка рубль бережёт
def take_small(money):
    return [x for x in money if x < 100]


"""
#Виртуальный кликер
__count = 0


def get_count():
    return __count


def click():
    global __count
    __count += 1