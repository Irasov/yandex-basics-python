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


#Подготовка данных
def to_string(*data, sep=" ", end="\n"):
    return sep.join(str(value) for value in data) + end



#Арифметический помощник
def get_operator(operator):
    if operator == "+":
        return lambda a, b: a + b 
    elif operator == "-":
        return lambda a, b: a - b
    elif operator == "*":
        return lambda a, b: a * b
    elif operator == "/":
        return lambda a, b: a / b
    elif operator == "**":
        return lambda a, b: a ** b
    elif operator == "//":
        return lambda a, b: a // b



#Подготовитель данных
def to_string(*data, sep=" ", end=""):
    return sep.join(str(value) for value in data) + end


def get_formatter(sep=" ", end=""):
    return lambda *data: to_string(*data, sep=sep, end=end)

    
   
#Странный рост
def grow(*args, **kwargs):
    result = list(args)
    for name, value in kwargs.items():
        length = len(name)
        for pos in range(len(result)):
            if args[pos] % length == 0:
                result[pos] += value
    return tuple(result)


#Странное произведение
def product(*args, **kwargs):
    keys = list(kwargs.keys())
    res = []
    for arg in args:
        list_values = []
        for k in keys:
            if k in arg:
                list_values.append(kwargs[k])
        if list_values:
            value = 1
            for v in list_values:
                value *= v
            res.append(value)
    return tuple(res)


"""
#Наилучший выбор
def choice(*args, **kwargs):
    if "min" in kwargs:
        func = kwargs["min"]
        min_max = min
    else:
        func = kwargs["max"]
        min_max = max
    return min_max(map(func, args))

result = choice(1, 2, 3, 4, 5, max=lambda x: 2 ** x)

print(result)