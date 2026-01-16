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


"""
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