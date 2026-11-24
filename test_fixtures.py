#Задача 1. Фикстура в тестовом файле (не в conftest.py)
import pytest

# @pytest.fixture
# def sample_bug():
#     return {'id': 1, 'severity': 'high', 'status': 'open'}

# def test_bug_severity(sample_bug):
#     assert sample_bug['severity'] == 'high'

# def test_bug_open(sample_bug):
#     assert sample_bug['status'] == 'open'

#Вопрос: почему фикстура в тестовом файле работает, хотя conftest.py нет? потому что pytest ищет файлы с префиксом test

#Задача 2. yield — temp-файл
import os

@pytest.fixture
def temp_file():
    path = 'fixture_temp.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write('test data')
    yield path
    if os.path.exists(path):
        os.remove(path)

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)

def test_file_content(temp_file):
    with open(temp_file, 'r', encoding='utf-8') as f:
        assert f.read() == 'test data'

#Вопрос: что будет, если убрать teardown (os.remove после yield)? Файл останется? Проверь — запусти, посмотри ls. Файл остается

#Задача 3. Перенос в conftest.py
def test_base_url(base_url):
    assert base_url.startswith('https')

#Вопрос: почему test_fixtures.py не импортирует conftest.py, а фикстуры видны? Потому что pytest ищет от текущей папки и ниже все тесты с префиксом test и фикстуры из файла conftest.py

#Задача 4. Зависимость фикстур
def test_endpoint(users_endpoint):
    assert users_endpoint == 'https://api.example.com/users'

#Вопрос: pytest сам вызовет base_url до users_endpoint? Почему порядок не твой? pytest сам вызовет base_url. Тест обращается к фикстуре users_endpoint, которая зависима от base_url

#Задача 5. scope='session' vs function
def test_a(per_test, once_per_run):
    print('test_a')

def test_b(per_test, once_per_run):
    print('test_b')

#Вопрос: почему once_per_run не пересоздаётся между test_a и test_b? Не понял вопроса

#Задача 6 (комплексная). conftest.py + несколько фикстур
def test_client_url(api_client):
    assert api_client['url'] == 'https://api.example.com'

def test_client_headers(api_client):
    assert 'Authorization' in api_client['headers']

def test_report_written(api_client, temp_report):
    with open(temp_report, 'w', encoding='utf-8') as f:
        f.write(f"URL: {api_client['url']}")
    with open(temp_report, 'r', encoding='utf-8') as r:
        result = r.read()
        assert 'https://api.example.com' in result

#Вопрос: почему api_client не создаётся дважды для test_client_url и test_client_headers? (Подсказка: scope по умолчанию — function.) Потому что scope по умолчанию function, а значит данные создаются каждый раз заново