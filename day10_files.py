# Задача 1. Записать и прочитать
with open('output.txt', 'w', encoding='utf-8') as out:
    out.write('line1\n')
    out.write('line2\n')
    out.write('line3\n')

with open('output.txt', 'r', encoding='utf-8') as out:
    for line in out:
        print(line.strip())

# Задача 2. JSON из файла
import json #импорт библиотеки

headers = {'status': 200, 'body': 'ok', 'headers': {'Content-Type': 'application/json'}}    #присвоение глобальной переменной значение словаря

with open('response.json', 'w', encoding='utf-8') as file: #открыть файл response.json в режиме Запись в кодировке utf-8
    json.dump(headers, file, ensure_ascii=False, indent=2) #сериализация словаря headers в файл file(элиас response.json), кириллица без экранирования, красивые отступы

with open('response.json', 'r', encoding='utf-8') as file:  #открыть файл response.json в режиме Чтение в кодировке utf-8
    response = json.load(file)  #присвоение переменной response прочтенного и распарсенного файла file(элиас response.json)

print(response['status']) #вывод ключа 'status' из переменной response
print(type(response))   #вывод типа переменной response

# Задача 3. CSV — список багов
import csv

text = [
    ['id', 'severity', 'status'],
    [1, 'high', 'open'],
    [2, 'low', 'closed'],
    [3, 'high', 'open']
]

with open('bugs.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(text)

high_count = 0
with open('bugs.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"bug {row['id']}: {row['severity']}")
        if row['severity'] == 'high':
            high_count += 1

print(f'high count: {high_count}')

# Задача 4. FileNotFoundError
def read_or_default(path, default=''):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return default
    
print(read_or_default('output.txt'))         # содержимое
print(read_or_default('missing.txt', 'no file'))  # 'no file'

# Задача 5 (посложнее). Записать отчёт
results = [
    {'name': 'test_login', 'status': 'PASSED'},
    {'name': 'test_logout', 'status': 'FAILED'},
    {'name': 'test_profile', 'status': 'PASSED'},
]

pass_count = 0
fail_count = 0
for result in results:
    if result['status'] == 'PASSED':
        pass_count += 1
    else:
        fail_count += 1

with open('report.txt', 'w', encoding='utf-8') as r:
    print('Test Report', file=r)
    print('---', file=r)
    for result in results:
        print(f"{result['name']}: {result['status']}", file=r)
    print('---', file=r)
    print(f'Passed: {pass_count}, Failed: {fail_count}', file=r)

# with open('report.txt', 'r', encoding='utf-8') as r:
#     for line in r:
#         print(line.strip())

