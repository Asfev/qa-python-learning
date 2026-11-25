import pytest


def parse_positive(value):
    """Приводит к int, требует > 0, иначе ValueError."""
    n = int(value)
    if n <= 0:
        raise ValueError(f'Not positive: {n}')
    return n


def check_status(code):
    """2xx → success, 3xx → redirect, 4xx → client error, 5xx → server error, иначе → unknown."""
    if 200 <= code < 300:
        return 'success'
    if 300 <= code < 400:
        return 'redirect'
    if 400 <= code < 500:
        return 'client error'
    if 500 <= code < 600:
        return 'server error'
    return 'unknown'

#Задача 1. pytest.raises — увидеть разницу
def test_parse_negative_without_raises():
        parse_positive('-5')     # бросит ValueError — что будет с тестом? Тест FAILED


def test_parse_negative_raises():
    with pytest.raises(ValueError):
        parse_positive('-5')    # ожидаемая ошибка по типу ValueError. Тест PASSED

# Вопрос: в чём разница между 1a и 1b? Почему 1a — FAILED, а 1b — PASSED? разница в pytest.raises.
# В первом тест падает из-за ошибки, отсюда FAILED. Во втором ожидаем ошибку, тест PASSED

#Задача 2. match — проверка сообщения
def test_negative_messages():
    with pytest.raises(ValueError, match='Not positive'):
        parse_positive('-5')


def test_zero_messages():
    with pytest.raises(ValueError, match='Not positive'):
        parse_positive('0')


def test_wrong_match():
    with pytest.raises(ValueError, match='totally wrong'):
        parse_positive('-5')

# Вопрос: почему 2c упал, хотя ValueError был брошен? Что не так с match? FAILED test_day13.py::test_wrong_match - AssertionError: Regex pattern did not match.
# ожидали в подтексте ошибки 'totally wrong', по факту получили 'Not positive: -5'

# Задача 3. as exc_info — точная проверка
def test_exc_info_str():
    with pytest.raises(ValueError) as exc_info:
        parse_positive('-5')
    assert str(exc_info.value) == 'Not positive: -5'


def test_exc_info_type():
    with pytest.raises(ValueError) as exc_info:
        parse_positive('-5')
    assert exc_info.type is ValueError

# Вопрос: чем str(exc_info.value) отличается от exc_info.type? Что каждое даёт?
# первое приводит значение объекта исключения в строку, второе это класс исключения. Строка = строка, Класс = ValueError

# Задача 4. parametrize — один тест, много данных
@pytest.mark.parametrize('code, expected', [
    (200, 'success'),
    (299, 'success'),        # граница
    (300, 'redirect'),       # граница
    (404, 'client error'),
    (500, 'server error'),
    (100, 'unknown'),
    (600, 'unknown'),
])
def test_check_status(code, expected):
    assert check_status(code) == expected

# Вопрос: сколько раз pytest вызвал check_status? Почему имена — [200-success], а не test_check_status 7 раз?
# 7 кортежей - 7 вызово. Имена присваиваются по умолчанию через repr

# Задача 5. parametrize + ids — читаемые имена
@pytest.mark.parametrize('code, expected', [
    (200, 'success'),
    (299, 'success'),
    (300, 'redirect'),
    (404, 'client error'),
    (500, 'server error'),
    (100, 'unknown'),
    (600, 'unknown'),
], ids=['200-ok', '299-ok', '300-redirect', '404-error', '500-error', '100-unknown', '600-unknown'])
def test_check_status_with_ids(code, expected):
    assert check_status(code) == expected

# Вопрос: в чём удобство ids? Когда без них неудобно?
# При выводе тестов сразу видно границы покрытия тестов. Когда много неоднозначных тестов

# Задача 6 (комплексная). parametrize + pytest.raises + match
@pytest.mark.parametrize('value, match', [
    ('-5', 'Not positive'),
    ('0', 'Not positive'),
    ('abc', 'invalid literal'),
], ids=['negative', 'zero', 'not-a-number'])
def test_parse_negative(value, match):
    with pytest.raises(ValueError, match=match):
        parse_positive(value)

# Вопрос: почему для 'abc' другое сообщение? Откуда invalid literal?
# Потому что при приведении через int строки 'abc' получаем ошибку типа ValueError содержащую подтекст с invalid literal, т.к. строку нельзя привести к целому числу