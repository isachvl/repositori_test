import pytest

@pytest.fixture()
def befor_after():
    print("before test")
    yield 
    print("After text")




def test_demo1():
    assert 1==1

def test_demo2(befor_after):
    assert 2==3
