def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int('200'))
print(safe_int('abc'))
print(safe_int('3.14'))


def divide_safe(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f'Ошибка: {e}')
        
print(divide_safe(10, 2))
print(divide_safe(10, 0))


responses = [
    {'status': 200, 'body': 'ok'},
    {'status': 500},
    {'status': 404, 'body': 'not found'},
]

for response in responses:
    try:
        print(response['body'])
    except KeyError:
        print('no body')


def process(code):
    try:
        return int(code)
    except ValueError:
        print('Not a number')
    finally:
        print('Processed')

print(process('200'))
print(process('abc'))


def validate_status(code):
    if 200 <= code < 300:
        return 'success'
    raise ValueError(f'Not success: {code}')
    
try:
    print(validate_status(200))     # вернёт 'success' — напечатать
    print(validate_status(404))     # бросит ValueError — поймать
except ValueError as e:
    print(f'Caught: {e}')


def flaky():
    # функция, которая "иногда" падает — для теста
    if flaky.attempts < 2:
        flaky.attempts += 1
        raise ValueError('not yet')
    return 'OK'

def retry(func, retries=3):
    for attempt in range(retries):
        try:
            return func()
        except ValueError:
            if attempt == retries - 1:
                raise


flaky.attempts = 0
print(retry(flaky))     # OK — со второй попытки