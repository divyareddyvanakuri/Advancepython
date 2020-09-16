import unittest
from moodeanalyzer import ModeAnalyzer

class TestMoodAnalyzer(unittest.TestCase):
    
    def test_analyzeMood_method_can_just_return_sad(self):
        #assume
        moodAnalyzer = ModeAnalyzer()
        #action
        result = moodAnalyzer.analyseMood("i am in sad mood")
        #assert
        assert "Sad" == result
    
    def test_analyzeMood_method_need_to_check_for_sad_else_return_happy(self):
        moodAnalyzer = ModeAnalyzer()
        result = moodAnalyzer.analyseMood("i am in any mood")
        assert "Happy" == result

if __name__ == "__main__":
    unittest.main()