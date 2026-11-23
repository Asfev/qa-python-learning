#Задача 1
def parse_status(value):
    try:
        code = int(value)
        return f'Status: {code} ({type(code).__name__})'
    except ValueError:
        return f'Invalid: {value} ({type(value).__name__})'

print(parse_status('200'))    # Status: 200 (int)
print(parse_status(404))      # Status: 404 (int)
print(parse_status('abc'))    # Invalid: abc (str)

#Задача 2
def is_present(value):
    return bool(value)
    
print(is_present(''))        # False
print(is_present('0'))       # True (непустая строка!)
print(is_present(0))         # False
print(is_present(None))      # False
print(is_present([1]))       # True
print(is_present([]))        # False
# почему is_present('False') → True? Потому что 'False' - непустая строка. Как во втором print

# #Задача 3
def classify_response(code):
    if code == 0:
        return 'no_response'
    elif 200 <= code < 300:
        return 'ok'
    elif 300 <= code < 400:
        return 'redirect'
    elif 400 <= code < 500:
        return 'client_error'
    elif 500 <= code < 600:
        return 'server_error'
    else:
        return 'unknown'
    
print(classify_response(200))   # ok
print(classify_response(0))     # no_response
print(classify_response(999))   # unknown
print(classify_response(-1))    # unknown

#Задача 4
codes = [200, 404, 500, 201, 302, 0, 204]

for i, code in enumerate(codes):
    if 200 <= code < 300:
        print(code)
    print(f'First non-2xx: {code} at index {i}')
    break
    
# почему после break коды 500, 201, ... не выводятся? Потому что break выводит из цикла немедленно

#Задача 5
response_codes = [500, 200, 404, 201, 302, 204, 500]

success_codes = []

for resp in response_codes:
    if 200 <= resp < 300:
        success_codes.append(resp)

count = 0 

for q in response_codes:
    if q == 500:
        count += 1

print(success_codes) #1
print(response_codes[:2]) #2
print(response_codes[::-1]) #3
print(f'500 count: {count}') #4
print(f'500 count: {response_codes.count(500)}') #4 встроенный метод для списков, подсчет значения
sorted_response_codes = sorted(response_codes)
print(f'sorted: {sorted_response_codes}') #5
print(f'302 in list: {302 in response_codes}') #6

#Задача 6
responses = [
    {'status': 200, 'body': 'ok'},
    {'status': 500, 'body': 'error'},
    {'status': 200, 'body': 'ok'},
    {'status': 404},
]

defaults = {'timeout': 5, 'retries': 3}
overrides = {'timeout': 10, 'base_url': 'https://api'}

count_statuses = {}

for response in responses:
    status = response['status'] #извлечь ключ 'status' из словаря responses
    count_statuses[status] = count_statuses.get(status, 0) + 1 #Запись в новый словарь значения key (200,500...) с присвоением ему значения начиная с 0

print(count_statuses) #1

for count in responses:
    print(count.get('body', 'no body')) #2

config = {**defaults, **overrides}
print(config) #3

#Задача 7
def make_response(status, body='ok', headers=None):
    if headers is None:
        headers = {}
    return {'status': status, 'body': body, 'headers': headers}


def summarize(*codes):
    return (min(codes), max(codes), len(codes))


def build_url(base, **params):
    if not params:
        return base
    query = '&'.join(f'{k}={v}' for k, v in params.items())
    return f'{base}?{query}'

print(make_response(200))                          # {'status': 200, 'body': 'ok', 'headers': {}}
print(make_response(404, 'not found'))             # {'status': 404, 'body': 'not found', 'headers': {}}
print(summarize(200, 404, 500))                    # (200, 500, 3)
print(build_url('/users', page=1, limit=10))       # /users?page=1&limit=10
print(build_url('/users')) #/users

#Задача 8
def safe_divide(a, b, default=None):
    try:
        return a / b
    except ZeroDivisionError:
        return default

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, 0, 0))    

def retry_until_success(func, retries=3):
    if retries < 1:
        raise ValueError('retries must be >= 1')
    for attempt in range(retries):
        try:
            return func()
        except ValueError:
            if attempt == retries - 1:
                raise


def validate_code(code):
    if 200 <= code < 300:
        return 'ok'
    raise ValueError(f'Bad code: {code}')

try:
    print(validate_code(200))
    print(validate_code(404))
except ValueError as e:
    print(f'Caught: {e}')


def flaky():
    if flaky.attempts < 2:
        flaky.attempts += 1
        raise ValueError('not yet')
    return 'OK'

flaky.attempts = 0
print(retry_until_success(flaky))    # ожидалось OK


def always_fails():
    raise ValueError('always')

try:
    retry_until_success(always_fails)
except ValueError as e:
    print(f'After retries: {e}')     # After retries: always

#Задача 9 выполнена в review_utils.py и review_main.py

#Задача 10
import json
import csv

data_json = [{'id': 1, 'status': 200}, {'id': 2, 'status': 404}]
data_csv = [{'id': 1, 'status': 200}, {'id': 2, 'status': 404}]

with open('review_data.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, ensure_ascii=False, indent=2)

with open('review_data.json', 'r', encoding='utf-8') as file:
    response = json.load(file)

for status in response:
    print(status['status'])

with open('review_data.csv', 'w', encoding='utf-8', newline='') as file:
    fields = ['id', 'status']
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data_csv)

with open('review_data.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for items in reader:
        print(f"id={items['id']}, status={items['status']}")

def read_json_or_default(path, default=None):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return default if default is not None else {}

print(read_json_or_default('review_data.json'))       # [{'id': 1, ...}, ...]
print(read_json_or_default('missing.json'))            # {}
print(read_json_or_default('missing.json', []))        # []
print(type(read_json_or_default('review_data.json')))   #<class 'list'>

#Задача 11
responses = [
    {'status': 200, 'body': 'ok'},
    {'status': 500, 'body': 'err'},
    {'status': 200, 'body': 'ok'},
]

def generate_report(responses, output_path):
    # TODO 1: счётчики
    counts = {}
    success = 0
    failed = 0
    
    # TODO 2: цикл по responses
    for response in responses:
        status = response['status']                                    # извлечь статус
        # TODO 2a: увеличить счётчик для этого status (паттерн "счётчик")
        counts['status'] = counts.get('status', 0) + 1
        # TODO 2b: success или failed?
        if 200 <= status < 300:
            success += 1
        else:
            failed += 1
    # TODO 3: записать в файл
    with open(output_path, 'w', encoding='utf-8') as f:
        # 5 строк через print(..., file=f)
        print('Report')
        print('---')
        print(f'Status counts: {counts}')
        print(f'Success: {success}, Failed: {failed}')
        print('---')
    
    # TODO 4: вернуть словарь
    return {'counts': counts, 'success': success, 'failed': failed}

result = generate_report(responses, 'review_report.txt')
print(result)