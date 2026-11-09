print('Hello, QA')
name = 'Alex'
print(f'Меня зовут {name}')

# print(type(200))
# print(type('200'))
# print(type(True))
# print(type(None))
# print(type(3.14))

# print(int("200"))     # → 200, из строки в число
# print(str(200))       # → "200", из числа в строку
# print(float("3.14"))  # → 3.14
# print(int(3.99))      # → 3, ОБРЕЗАЕТ дробную часть, не округляет!
# print(bool(-1))        # → False, bool(1) → True, bool("") → False, bool("abc") → True

age = input("Введите возраст: ")   # age = "25", тип str
age_int = int(age)                 # age_int = 25, тип int
#print(age + 1)                     # ОШИБКА: TypeError, нельзя str + int
print(age_int + 1)                 # 26, работает