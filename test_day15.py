# Задача 1. skip — тест не выполняется
import pytest


@pytest.mark.skip(reason='функция ещё не реализована — BUG-100')
def test_future_feature():
    print('\n[ЭТО НЕ ДОЛЖНО НАПЕЧАТАТЬСЯ]')
    assert False


def test_working():
    assert 1 + 1 == 2

# Задача 2. skipif — условный пропуск
import sys
import pytest


@pytest.mark.skipif(sys.platform == 'win32', reason='только Linux/Mac')
def test_unix_only():
    assert '/' in '/tmp/test'


@pytest.mark.skipif(sys.platform != 'win32', reason='только Windows')
def test_windows_only():
    assert '\\' in 'C:\\temp'

# Задача 3. xfail — ожидаемо падает
import pytest


@pytest.mark.xfail(reason='BUG-200: ещё не исправлен', strict=True)
def test_known_bug():
    print('\n[ЭТО ДОЛЖНО НАПЕЧАТАТЬСЯ]')
    assert 1 + 1 == 3


@pytest.mark.xfail(reason='BUG-201: думаем, что сломан', strict=True)
def test_actually_works():
    assert 1 + 1 == 2

# Задача 4. pytest.skip() — внутри теста
import pytest


def external_api_available():
    # имитация: возвращает False
    return False


def test_external_api():
    if not external_api_available():
        pytest.skip('Внешний API недоступен')
    assert True


def test_internal_always_runs():
    assert True

# Задача 5. pytest.ini + свои маркеры + -m
@pytest.mark.smoke
def test_smoke_health():
    assert True


@pytest.mark.slow
def test_slow_query():
    assert True


@pytest.mark.regression
@pytest.mark.slow
def test_regression_full_flow():
    assert True

# Задача 6 (комплексная). Всё вместе
import sys
import pytest


# 1. безусловный skip
@pytest.mark.skip(reason='не реализовано')
def test_unimplemented():
    assert False


# 2. условный skipif
@pytest.mark.skipif(sys.platform != 'linux', reason='только Linux')
def test_linux_only():
    assert True


# 3. xfail strict
@pytest.mark.xfail(reason='BUG-999', strict=True)
def test_known_fail():
    assert False


# 4. программный skip
def test_dynamic_skip():
    if not True:                          # условие: False
        pytest.skip('не сработает')
    assert True


# 5. маркеры + фильтр
@pytest.mark.smoke
def test_smoke():
    assert True


@pytest.mark.slow
def test_slow():
    assert True