name = input('Введите имя: ')
age = input('Введите возраст: ')
age = int(age)
print(f'Привет, {name}, тебе {age} лет')

days = age*365
print(f'Ты прожил примерно {days} дней')

print(type(name)) #<class 'str'>
print(type(age))    #<class 'int'>
print(type(days))   #<class 'int'>
print(type(365))    #<class 'int'>
print(type('')) #<class 'str'>

status = '200'
print(type(status)) #<class 'str'>
print(status == 200)    #False
print(int(status) == 200)   #True

print(bool("")) #False
print(bool("False"))    #True
print(bool(0)) #False
print(bool(-1)) #True
print(bool(None))   #False
print(int(3.99))    #3