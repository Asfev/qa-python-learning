print("open" in ["open", "closed"])    # True — есть ли "open" в списке
print("@" in "test@mail.com")            # True — есть ли "@" в строке
print("x" in "abc")                      # False
print(200 in [200, 201, 202])            # True
print("x" not in "abc")     # True — "x" нет в строке

# if условие1:
    # блок 1 — выполнится, если условие1 True
# elif условие2:
    # блок 2 — если условие1 False, а условие2 True
# elif условие3:
    # блок 3 — если все выше False, а условие3 True
# else:
    # блок 4 — если все условия выше False
x = 5
if x > 5:
    print('ok')
elif x == 5:
    print('equal')
else:
    print('not ok')

responseStatus = 799

if responseStatus >= 200 and responseStatus < 300:
    print('success')
elif responseStatus >= 300 and responseStatus < 400:
    print('redirect')
elif responseStatus >= 400 and responseStatus < 500:
    print('client error')
elif responseStatus >= 500 and responseStatus < 600:
    print('server error')
else:
    print('unknown')


responseStatus = -1

if 200 <= responseStatus < 300:
    print('success')
elif 300 <= responseStatus < 400:
    print('redirect')
elif 400 <= responseStatus < 500:
    print('client error')
elif 500 <= responseStatus < 600:
    print('server error')
else:
    print('unknown')


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

result = check_status(303)

print(result)


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if len(email) <= 5:
        return False
    if '@' not in email:
        return False
    if '.' not in email.split("@")[-1]:
        return False
    return True

print(is_valid_email('eden@bk.ru'))


def age_category(age):
    if age < 0:
        return 'invalid' 
    elif 0 <= age < 18:
        return 'ребёнок'
    elif 18 <= age < 65:
        return 'взрослый'
    else:
        return 'пенсионер'
    
print(age_category(-1))    # invalid
print(age_category(0))     # ребёнок
print(age_category(17))    # ребёнок
print(age_category(18))    # взрослый
print(age_category(64))    # взрослый
print(age_category(65))    # пенсионер
print(age_category(100))   # пенсионер