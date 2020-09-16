import re

class Registeration:

    def __init__(self,firstname=None,email=None,mobilenumber=None):
        self.firstname = firstname
        self.email = email
        self.mobilenumber = mobilenumber

    def firstNameValidator(self):
        try:
            pattren = re.compile("[A-Z][a-z]{3,12}")
            if pattren.match(self.firstname):
                return "valid"
            return "invalid"
        except (TypeError,NameError):
            return None

    def emailValidator(self):
        try:
            pattren = re.compile("^[\w*]+[\._]?[\w*]+[@]\w+[.]\w{2,3}(.[a-z]{2})?$")
            if pattren.match(self.email):
                return "valid"
            return "invalid"
        except (TypeError):
            return None
    

    def mobilenumberValidator(self):
        pattern = re.compile("^(91)\s[7-9][0-9]{9}")
        if pattern.match(self.mobilenumber):
            return True
        return False


