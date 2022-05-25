#pip install -U pytest
#Test-script names must be pre or postfixed with test_
# e.g. test_myTests.py or myTests_test.py
# invoke from console: >pytest <optional test_...py>
# from a .py: retcode = pytest.main()
import pytest
import sys, pathlib
#result = pytest.main(sys.argv) # just this file
result = pytest.main(pathlib.Path(sys.argv[0]).parent) # script directory

def foo(x):
    return x+1

#Class name must start with Test
#functions must be prefixed with test_
class TestFoo:

    def test_foo(s):
        assert foo(1) == 2

    def test_fooFail(s):
        assert foo(2) == 2