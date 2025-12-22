'''
#Символическая разница
a = set(input())
b = set(input())
ab = a & b
for n in ab:
    print(n, end="")

    
#Зайка-8
count = int(input())
names = set()
for _ in range(count):
    locality = input().split()
    for loc in locality:
        names.add(loc)
for name in names:
    print(name)


#Кашееды
m = int(input())
o = int(input())
group1 = set()
group2 = set()
for _ in range(m):
    group1.add(input())
for _ in range(o):
    group2.add(input())
if len(group1 & group2) != 0:
    print(len(group1 & group2))
else:
    print('Таких нет')


#Кашееды — 2
interection = set()
m = int(input())
o = int(input())
group = set()
for _ in range(m + o):
    group.add(input())
res = abs(m + o - (2 * (len(group))))
if res == 0:
    print('Таких нет')
else: 
    print(res)


#Кашееды — 3
interection = set()
m = int(input())
o = int(input())
group = set()
for _ in range(m + o):
    name = input()
    if name in group:
        group.remove(name)
    else:
        group.add(name)
if len(group) == 0:
    print('Таких нет')
else:
    sorted_res = list(group)
    sorted_res.sort()
    for s in sorted_res:
        print(s)


#Азбука Морзе
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 
    'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.'
}
text = input().upper()
res = ""
for ch in text:
    if ch in morse:
        res += morse[ch] + " "
    elif ch == " ":
        res += "\n"
print(res)


#Кашееды — 4
lists = {}
for _ in range(int(input())):
    name, *porridge = input().split()
    lists[name] = porridge
find = input()
names = []
for name in lists:
    if find in lists[name]:
        names.append(name)
if len(names) == 0:
    print("Таких нет")
else:
    names.sort()
    for name in names:
        print(name)


#Зайка — 9
place = input().split()
objects = {}
while len(place) != 0:
    for pl in place:
        if pl in objects:
            objects[pl] += 1
        else:
            objects[pl] = 1
    place = input().split()
for obj in objects:
    print(obj, objects[obj], sep=" ")


#Однофамильцы
surnames = {}
count = 0
for _ in range(int(input())):
    surname = input()
    if surname in surnames:
        surnames[surname] += 1
    else:
        surnames[surname] = 1
for sur in surnames:
    if surnames[sur] > 1:
        count += surnames[sur]
print(count)


#Однофамильцы-2
surnames = {}
count = True
for _ in range(int(input())):
    surname = input()
    if surname in surnames:
        surnames[surname] += 1
    else:
        surnames[surname] = 1
surnames = dict(sorted(surnames.items()))
for sur in surnames:
    if surnames[sur] > 1:
        print(sur, surnames[sur], sep=' - ')
        count = False
if count:
    print("Однофамильцев нет")
'''


#Транслитерация
TRANSLITERATE_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}
result = ''
for char in input():
    char_copy = char.upper()
    if char_copy in TRANSLITERATE_DICT:
        if char.isupper():
            char = TRANSLITERATE_DICT[char_copy].capitalize()
        else:
            char = TRANSLITERATE_DICT[char_copy].lower()
    result += char

print(result)