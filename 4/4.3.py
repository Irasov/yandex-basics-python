"""
#Рекурсивный сумматор

def recursive_sum(*args):
    if not args:
        return 0
    return recursive_sum(*args[:-1]) + args[-1]

result = recursive_sum(1, 2, 3)
print(result)  # 6


#Рекурсивный сумматор цифр
def recursive_digit_sum(number):
    if not number:
        return 0
    return recursive_digit_sum(number // 10) + number % 10

result = recursive_digit_sum(7321346)
print(result)  # 26



#Многочлен N-ой степени
def make_equation(*args):
    if len(args) == 1:
        return args[0]
    return "(" + str(make_equation(*args[:-1])) + ") * x + " + str(args[-1])
result = make_equation(3, 1, 5, 3)
print(result)  # "(((3)*x + 1)*x + 5)*x + 3"


#Декор результата
def answer(func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"
    return new_func

@answer
def a_plus_b(a, b):
    return a + b
print(a_plus_b(3, 5))
print(a_plus_b(7, 9))


#Накопление результата
def result_accumulator(func):
    results = []

    def new_func(*args, method="accumulate"):
        if method == "accumulate":
            results.append(func(*args))
            return None
        else:
            results.append(func(*args))
            res = results.copy()
            results.clear()
            return res

    return new_func


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))


#Сортировка слиянием
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

result = merge_sort([3, 2, 1])
print(result)  # [1, 2, 3]


#Сортировка слиянием
def same_type(func):
    def new_func(*args):
        first_type = type(args[0])
        if all(type(el) == first_type for el in args):
            return func(*args)
        else:
            print("Обнаружены различные типы данных")
    return new_func


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')


"""
#Генератор Фибоначчи
def fibonacci(n):
    n_1, n_2 = 0, 1
    for _ in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2

print(*fibonacci(5))