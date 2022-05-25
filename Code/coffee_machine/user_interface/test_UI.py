from  user_io import *

class Test_getIntSequence:
    def test_input_all_nums(s):
        assert getIntSequence("","1 2 3 4") == [1,2,3,4]

    def test_input_last_char(s):
        assert getIntSequence("","1 2 3 f") == [1,2,3]
    
    def test_input_first_char(s):
        assert getIntSequence("","A 1 2 3") == [1,2,3]
    
    def test_input_l_space(s):
        assert getIntSequence("","  1 2 3") == [1,2,3]
            
    def test_input_r_space(s):
        assert getIntSequence("","1 2 3  ") == [1,2,3]