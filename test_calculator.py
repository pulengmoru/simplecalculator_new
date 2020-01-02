from calculator import add


def test_add():
    results = add(1, 2)
    assert result == 3

from calculator import divide

def test_divide():
    results = divide(9, 3)
    assert result == 3


def test_divide_by_zero():
    results = divide(99, 0)
    assert type(result) == str

    from calculator import multiply


def test_multiply():
    results = multiply(6, 1)
    assert result == 6
    rint(result)

 from calculator import subtract


def test_subtract():
    result = subtract(5, 2)
    assert result == 3   