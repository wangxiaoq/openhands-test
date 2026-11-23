from main import add, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(3, 2) == 1
    assert sub(1, 5) == -4
    assert sub(0, 0) == 0