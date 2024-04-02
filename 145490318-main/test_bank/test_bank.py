from bank import value

def test_value_hello():
    result = value("hello, world")
    assert result == 0

def test_value_h():
    result = value("hi there")
    assert result == 20

def test_capital():
    result = value ("Hi there")
    assert result == 20

def test_capital_2():
    result=value("Hello world")
    assert result == 0

def test_value_other():
    result = value("something else")
    assert result == 100
