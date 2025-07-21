"""Задача 3
Вам дана строка:

text = 'Цвет неба - синий.'
Напишите и примените регулярное выражение, чтобы заменить все вхождения слова
синий
 на слово
blue
"""

import re

text = 'Цвет неба - синий.'

pattern = re.compile(r'синий')

result = pattern.sub('blue', text)

print(result)