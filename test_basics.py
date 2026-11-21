def test_math():
    assert 2 + 2 == 4

def test_math_failing():
    assert 2 + 2 == 5

def test_with_messages():
    expected = 200
    actual = 500
    assert expected == actual, f'Ожидали {expected}, получили {actual}'