from src.app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("All tests passed!")
from src.app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("All tests passed!")
    
test_add()