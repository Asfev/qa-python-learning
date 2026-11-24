import pytest
import os

@pytest.fixture
def sample_bug():
    return {'id': 1, 'severity': 'high', 'status': 'open'}

@pytest.fixture
def base_url():
    return 'https://api.example.com'

@pytest.fixture
def users_endpoint(base_url):
    return f'{base_url}/users'

@pytest.fixture
def per_test():
    print('\n[SETUP per_test]')
    yield {'data': 1}
    print('[TEARDOWN per_test]')

@pytest.fixture(scope='session')
def once_per_run():
    print('\n[SETUP once_per_run]')
    yield {'config': 'https://api'}
    print('[TEARDOWN once_per_run]')

@pytest.fixture
def auth_headers():
    return {'Authorization': 'token abc123', 'Content-Type': 'application/json'}

@pytest.fixture
def api_client(base_url, auth_headers):
    return {'url': base_url, 'headers': auth_headers}

@pytest.fixture
def temp_report():
    path = 'api_report.txt'
    with open(path, 'w', encoding='utf-8') as f:
        pass
    yield path
    if os.path.exists(path):
        os.remove(path)