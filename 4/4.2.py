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

#Функциональный нод 2.0
def gcd(*args):
    a = args[0]
    for b in args[1:]:
        while b:
            a, b = b, a % b
    return a

    

#Имя of the month 2.0
def month(number, language="ru"):
    monts = {
        "ru": [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ],
        "en": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    }
    return monts[language][number - 1]


"""
#Подготовка данных
def to_string(*data, sep=" ", end="\n"):
    return sep.join(str(value) for value in data) + end