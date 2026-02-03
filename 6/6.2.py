"""
"""
#Длины всех слов - 2
import pandas as pd
import re
def length_stats(str):
    str = str.lower()
    str = re.sub(r'[^a-zа-яё\s]', '', str)
    words = set(str.split())
    words = list(words)
    words.sort()
    return pd.Series(map(len, words), index=words, dtype='int64')
print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))