
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


#Виртуальный кликер
__count = 0


def get_count():
    return __count


def click():
    global __count
    __count += 1


#Странная игра
__sum = 0


def move(player, number):
    global __sum
    if player == "Петя":
        __sum += number
    elif player == "Ваня":
        __sum -= number


def game_over():
    if __sum > 0:
        return "Петя"
    elif __sum < 0:
        return "Ваня"
    else:
        return "Ничья"
    

#Максимальный максимум
def max2D(matrix):
    return max(max(row) for row in matrix)

    
#Числовое фрагментирование
def fragments(numbers):
    res = []
    list_fragment = []
    current = -1000000000
    for i in range(len(numbers)):
        if numbers[i] > current:
            list_fragment.append(numbers[i])
            current = numbers[i]
        elif numbers[i] <= current:
            res.append(list_fragment)
            list_fragment = []
            list_fragment.append(numbers[i])
            current = numbers[i]
        if i == len(numbers) - 1 and len(list_fragment) > 0:
            res.append(list_fragment)
    return res
print(fragments([0, 4, 5, -9, -6, 3, 2, 3, 4, 9]))


#Имя of the month
def month(number, language):
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


#Числовая строка
def split_numbers(text):
    return tuple(int(i) for i in text.split())


"""
#Поиск гор
def find_mountains(heights):
    mountains = []
    for index, (left, middle, right) in enumerate(
        zip(heights, heights[1:], heights[2:]), 2
    ):
        if middle > left and middle > right:
            mountains.append(index)
    return tuple(mountains)