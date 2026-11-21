from utils import safe_int, check_status

def test_safe_int_valid():
    assert safe_int('200') == 200

def test_safe_int_invalid():
    assert safe_int('abc') is None

def test_safe_float_string():
    assert safe_int('3.14') is None

def test_200_is_success():
    assert check_status(200) == 'success'

def test_299_is_success():
    assert check_status(299) == 'success'

def test_300_is_redirect():
    assert check_status(300) == 'redirect'
    
def test_404_is_client_error():
    assert check_status(404) == 'client error'

def test_500_is_server_error():
    assert check_status(500) == 'server error'

def test_100_is_unknown():
    assert check_status(100) == 'unknown'

def test_600_is_unknown():
    assert check_status(600) == 'unknown'