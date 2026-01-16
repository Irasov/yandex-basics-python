"""
#Рекурсивный сумматор

def recursive_sum(*args):
    if not args:
        return 0
    return recursive_sum(*args[:-1]) + args[-1]

result = recursive_sum(1, 2, 3)
print(result)  # 6

"""
#Рекурсивный сумматор цифр
def recursive_digit_sum(number):
    if not number:
        return 0
    return recursive_digit_sum(number // 10) + number % 10

result = recursive_digit_sum(7321346)
print(result)  # 26