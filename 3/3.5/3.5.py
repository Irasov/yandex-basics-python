'''
#A+B+...
from sys import stdin
res = []
for line in stdin:
    numbers = map(int, line.split())
    [res.append(n) for n in numbers]
print(sum(res))



#Средний рост
from sys import stdin
res = []
s = 0
n = 0
for line in stdin:
    numbers = line.split()
    s += int(numbers[2]) -  int(numbers[1])
    n += 1 
print(round(s / n))


#Без комментариев 2.0
from sys import stdin
res = ''
text = []
for line in stdin:
    text.append(line)
for str in text:
    if str.startswith('#'): 
        pass
    elif str.find('#') != -1 and str.find('#') != 0:
        res += str[:str.find('#')].rstrip() + '\n'
    else: 
        res += str.rstrip() + '\n'
print(res)


#Найдётся всё 2.0
from sys import stdin
text = []
for line in stdin:
    text.append(line.strip())
for i in range(len(text) - 1):
    if text[-1].lower() in text[i].lower():
        print(text[i], end='\n')


#А роза упала на лапу Азора 6.0
from sys import stdin
text = []
res = []
for line in stdin:
    words = line.split()
    text.append(words)
for str in text:
    for word in str:
        if word.lower() == word[::-1].lower() and word not in res:
            res.append(word)
res.sort()
for w in res:
    print(w)


#А роза упала на лапу Азора 6.0
TRANSLITERATE_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}
lines = ""
transliterated_line = ""
with open("cyrillic.txt", encoding="utf-8") as file_in:
    for line in file_in:
        lines += line
for char in lines:
    if char.upper() in TRANSLITERATE_DICT:
        transliterated_line += (
            TRANSLITERATE_DICT[char.upper()].lower().capitalize()
            if char == char.upper()
            else TRANSLITERATE_DICT[char.upper()].lower()
        )
    else:
        transliterated_line += char
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(transliterated_line, file=file_out)


#Файловая статистика
fileName = input()
numbrs = []
positive = 0
with open(fileName) as file:
    numbers = [int(x) for x in file.read().split()]
for i in numbers:
    if i > 0:
        positive += 1 
print(len(numbers))
print(positive)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))


#Файловая разница
first = input()
second = input()
answer = input()
with open(first, encoding="utf-8") as file:
    setFist = {x for x in file.read().split()}
with open(second, encoding="utf-8") as file:
    setSecond = {x for x in file.read().split()}
res = setFist ^ setSecond
with open(answer, "w", encoding="UTF-8") as file_out:
    print('\n'.join(sorted(res)), file=file_out)

'''
#Файловая чистка
first = input()
second = input()
data = []
res = []
with open(first, encoding="utf-8") as file:
    for string in file:
        data.append(string.strip().replace("\t", "").split())
for i in data:
    if len(i) > 0:
        res.append(i)
with open(second, "w", encoding="UTF-8") as file:
    for str in res:
        print(" ".join(str), file=file)