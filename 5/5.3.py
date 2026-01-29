"""
#Обработка ошибок
def func():
    x = int('Hello, world!')
    
try: 
    func()
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
else:
    print("No Exceptions")



#Ломать — не строить
a = None
b = 9

func(a, b)


#Ломать — не строить 2
class Initiator:
    
    def __repr__(self) -> str:
        raise Exception


init = Initiator()
func(init)


#Контроль параметров
def only_positive_even_sum(a, b):
    if not (isinstance(a, int) or isinstance(b, int)):
        raise TypeError
    if a < 0 or b < 0 or a % 2 != 0 or b % 2 != 0:
        raise ValueError
    return a + b

print(only_positive_even_sum(3,2))


#Слияние с проверкой
def check_iter(*items):
    for item in items:
        try:
            iter(item)
        except TypeError:
            raise StopIteration


def check_type(*items):
    arr = []
    for item in items:
        arr.extend(list(item))
    one = arr[0]
    for val in arr:
        if type(one) != type(val):
            raise TypeError


def check_sort(*items):
    for item in items:
        if list(item) != sorted(item):
            raise ValueError


def merge(items_1, items_2):
    check_iter(items_1, items_2)
    check_type(items_1, items_2)
    check_sort(items_1, items_2)
    arr_1 = list(items_1)
    arr_2 = list(items_2)
    arr = []
    while arr_1 and arr_2:
        if arr_1[0] > arr_2[0]:
            arr.append(arr_2.pop(0))
        else:
            arr.append(arr_1.pop(0))
    arr.extend(arr_1 + arr_2)
    return arr


 """
#Корень зла 2 
class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    roots = ()
    if not all(type(n) in (int, float) for n in (a, b, c)):
        raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError('Infinite solutions')
    elif a == 0 and b != 0 and c != 0:
        roots = (-(c / b), -(c / b))
    elif a == b == 0:
        raise NoSolutionsError('No solution')
    elif a == c == 0:
        roots(0, 0)
    else:
        disc = (b ** 2) - (4 * a * c)
        if disc == 0:
            roots = ((-b) / (2 * a), (-b) / (2 * a))
        elif disc > 0:
            x1 = (-b - (disc ** 0.5)) / (2 * a)
            x2 = (-b + (disc ** 0.5)) / (2 * a)
            roots = tuple(sorted([x1, x2]))
        else:
            raise NoSolutionsError('No solution')
    return roots