# Задача 1. params + request.param
import pytest


@pytest.fixture(params=['https://api.dev', 'https://api.staging', 'https://api.prod'], ids=['dev', 'staging', 'prod'])
def base_url(request):
    return request.param


def test_url_https(base_url):
    assert base_url.startswith('https://')


def test_url_contains_api(base_url):
    assert 'api' in base_url

# Задача 2. request.param — обработка
@ pytest.fixture(params=[200, 404, 500], ids=['ok', 'not found', 'server-error'])
def response(request):
    return {'status': request.param, 'body': 'mocked'}


def test_status_valid(response):
    assert response['status'] in [200, 404, 500]


def test_body_present(response):
    assert response['body'] == 'mocked'

# Задача 3. indirect=True — параметры через фикстуру
@pytest.fixture
def user_id(request):
    return {'id': request.param, 'name': f'user_{request.param}'}


@pytest.mark.parametrize('user_id', [1, 2, 3], indirect=True)
def test_user_name(user_id):
    assert user_id['name'].startswith('user_')


@pytest.mark.parametrize('user_id', [1, 2, 3], indirect=True)
def test_user_id(user_id):
    assert user_id['id'] in [1, 2, 3]

# Задача 4. indirect — сравнение с обычным
@pytest.mark.parametrize('value', [1, 2, 3])
def test_direct(value):
    assert isinstance(value, int)       # напрямую — число


@pytest.fixture
def wrapped(request):
    return {'value': request.param}


@pytest.mark.parametrize('wrapped', [1, 2, 3], indirect=True)
def test_indirect(wrapped):
    assert isinstance(wrapped, dict)    # через фикстуру — словарь

# Задача 5. params × parametrize — комбинация
@pytest.fixture(params=['dev', 'prod'], ids=['env-dev', 'env-prod'])
def env(request):
    return request.param


@pytest.mark.parametrize('method', ['GET', 'POST'])
def test_request(env, method):
    assert env in ['dev', 'prod']
    assert method in ['GET', 'POST']

# Задача 6 (комплексная). params + indirect + yield
import pytest
import os


@pytest.fixture(params=['file_a.txt', 'file_b.txt'], ids=['a', 'b'])
def temp_file(request):
    path = request.param
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'content for {path}')
    yield path
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def file_content(request):
    return {'content': f'processed: {request.param}'}


@pytest.mark.parametrize('file_content', ['data1', 'data2'], indirect=True)
def test_combined(temp_file, file_content):
    assert os.path.exists(temp_file)
    assert 'processed:' in file_content['content']