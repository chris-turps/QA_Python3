#pip install -U pytest
#Test-script names must be pre or postfixed with test_
# e.g. test_myTests.py or myTests_test.py
# invoke from console: >pytest <optional test_...py>
# from a .py: retcode = pytest.main()
import pytest
import sys, pathlib
#result = pytest.main(sys.argv) # just this file
result = pytest.main(pathlib.Path(sys.argv[0]).parent)
# will search script folder for all test scripts

def foo(x):
    return x+1

#Class name must start with Test
#functions must be prefixed with test_
class TestFoo:

    def test_foo(s):
        assert foo(1) == 2

    def test_fooFail(s):
        assert foo(2) == 2

# Setup the context for tests using fixtures:
class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

# write the tests
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket