import unittest
from userregistration import Registeration

class TestUserRegisteration(unittest.TestCase):

    def test_givenfname_start_with_cap_and_has_mini_three_charas_then_should_return_valid(self):
        register = Registeration("Divya")
        result = register.firstNameValidator()
        assert "valid" == result
    def test_givenfname_start_without_cap_and_has_mini_three_charas_then_should_return_invalid(self):
        register = Registeration("divya")
        result = register.firstNameValidator()
        assert "invalid" == result
    def test_givenfname_start_with_cap_and_has_mini_less_than_three_charas_should_return_false(self):
        register = Registeration("Di")
        result = register.firstNameValidator()
        assert "invalid" == result
    def test_givenname_is_emptystring_then_should(self):
        register = Registeration("")
        result = register.firstNameValidator()
        assert "invalid" == result
    def test_givenfname_is_null_then_should_return_None(self):
        register = Registeration()
        result = register.firstNameValidator()
        assert None == result
    def test_givenfname_is_numeric_then_should_return_None(self):
        register = Registeration(12345)
        result = register.firstNameValidator()
        assert None == result
    def test_givenemail_without_optional_elements_then_should_return_valid(self):
        register = Registeration("divya","divya@gmail.com")
        result = register.emailValidator()
        assert "valid" == result
    def test_givenemail_with_optional_elements_then_should_return_valid(self):
        register = Registeration("divya","divya.123@gmail.com")
        result = register.emailValidator()
        assert "valid" == result
    def test_givenemail_is_emptystring_then_should_return_invalid(self):
        register = Registeration("divya","")
        result = register.emailValidator()
        assert "invalid" == result
    def test_givenemail_is_numeric_then_should_return_None(self):
        register = Registeration("divya",12345)
        result = register.emailValidator()
        assert None == result
    def test_givenemail_is_null_then_should_return_None(self):
        register = Registeration("divya")
        result = register.emailValidator()
        assert None == result
    
    
            
if __name__ == "__main__":
    unittest.main()