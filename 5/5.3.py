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


"""
#Контроль параметров
def only_positive_even_sum(a, b):
    if not (isinstance(a, int) or isinstance(b, int)):
        raise TypeError
    if a < 0 or b < 0 or a % 2 != 0 or b % 2 != 0:
        raise ValueError
    return a + b

print(only_positive_even_sum(3,2))

        
    
