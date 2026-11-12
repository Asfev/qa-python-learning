for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)


for code in [200, 404, 500, 201, 302, 204]:
    if 200 <= code < 300:
        print(code)



def check_status(code):
    if 200 <= code < 300:
        return 'success'
    elif 300 <= code < 400:
        return 'redirect'
    elif 400 <= code < 500:
        return 'client error'
    elif 500 <= code < 600:
        return 'server error'
    else:
        return 'unknown'
    
for code in [200, 301, 404, 503, 100]:
    check_status
    print(f'{code} -> {check_status(code)}')


bugs = [
    {'id': 1, 'status': 'open'},
    {'id': 2, 'status': 'closed'},
    {'id': 3, 'status': 'open'},
    {'id': 4, 'status': 'in progress'},
    {'id': 5, 'status': 'open'},
]

counts = {} #Создаем пустой словарь counts
for bug in bugs:
    status = bug['status'] #Для каждого ключа status из списка bugs присваиваем значение переменной status, взятое значение по ключу status
    counts[status] = counts.get(status, 0) + 1
#Для нашего пустого словаря записываем значения по переменной status. Новая запись идет по логике "взять в словаре counts status, если нет, то 0" и прибавляем 1

print(counts) #Вывести словарь


counts = {}
for bug in bugs:
    status = bug['status']
    if status in counts: #Если переменная status есть в словаре counts
        counts[status] = counts[status] + 1 #Если true, то обновляем запись, прибавляя 1
    else:
        counts[status] = 1 #Если false, то записываем 1

print(counts) #Вывести словарь
