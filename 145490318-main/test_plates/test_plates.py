from plates import is_valid

def test_capital_start():
    result=is_valid("HELLO")
    assert result==True

def test_pun():
    result=is_valid("HEllo, world")
    assert result==False
def test_length():
    result=is_valid("GOODBYE")
    assert result==False
#def test_start():
 #   assert result=is_valid("12hel")
  #  assert result == False
#def test_num():
 #   assert result=is_valid("w1y")
  #  assert result == False