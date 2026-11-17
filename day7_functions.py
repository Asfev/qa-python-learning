def make_bug(id, status='open', severity='medium'):
    return {'id': id, 'status': status, 'severity': severity}

print(make_bug(42))
print(make_bug(42, status = 'closed'))
print(make_bug(42, severity = 'high'))


def stats(*numbers):
    if numbers == ():
        return 'Empty'
    return min(numbers), max(numbers), sum(numbers)

print(stats(1, 5, 3))
print(stats(10, 20))
print(stats())


def make_request(url, **options):   
    return f'{url} with {options}'

print(make_request('/users'))
print(make_request('/users', timeout = 10, method = 'GET'))


def divide(a, b):
    return (a // b, a % b)

q, r = divide(10, 3)
print(f'Result = {q}, remainder = {r}')
q, r = divide(20, 4)
print(f'Result = {q}, remainder = {r}')


x = 'global'

def outer():
    x = 'local'
    print(x)

outer() #local, т.к при вызове функции outer переменной x присваивается строка local и затем выводится, отношения к ранее объявленной переменной x не имеет
print(x)    #global, т.к. переменная x в функции outer объявлена локально и существует только при её выполнении

