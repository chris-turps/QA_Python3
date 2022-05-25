from  .user_io import *

class Test_getIntSequence:
    def test_input_all_nums(s):
        assert getIntSequence("","1 2 3 4") == [1,2,3,4]

    def test_input_some_chars(s):
        assert getIntSequence("","a 1 2 b 3 f") == [1,2,3]
    
    def test_input_some_spaces(s):
        assert getIntSequence("","  1     2 3 ") == [1,2,3]
            
    def test_input_empty(s):
        assert getIntSequence("","") == []

