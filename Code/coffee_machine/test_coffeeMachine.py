#pip install -U pytest
#Test-script names must be pre or postfixed with test_
# e.g. test_myTests.py or myTests_test.py
# invoke from console: >pytest <optional test_...py>
# from a .py: retcode = pytest.main()
import pytest
import sys, pathlib
#result = pytest.main(sys.argv) # just this file
result = pytest.main(pathlib.Path(sys.argv[0]).parent) # script directory