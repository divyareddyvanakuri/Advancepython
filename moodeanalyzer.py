class ModeAnalyzer:

    def analyseMood(self,message):
        if message.__contains__("sad"):
            return "Sad"
        return "Happy"
