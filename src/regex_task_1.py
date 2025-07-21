"""Задача 1
Вам дан текст сообщения:

text = '''
Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com
'''
Напишите и примените регулярное выражение, чтобы получить список всех URL-адресов.
"""

import re
from re import Match
from typing import Iterator

text = '''
Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com
'''


def list_url(string: str) -> Iterator[Match[str]]:
    pattern = re.compile(r'www\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}')
    result = pattern.finditer(string)

    return result

lists = list_url(text)

for match in lists:
    print(match)