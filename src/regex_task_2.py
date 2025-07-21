import re


text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

result = pattern.findall(text)

print(result)