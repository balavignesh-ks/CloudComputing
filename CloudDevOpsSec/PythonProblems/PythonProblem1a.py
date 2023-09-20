class Person:

    full_Name=input("Enter your Name?\n")
    
#    def __init__(self, Name):
#        self.full_Name = Name

#    def welcome_msg(self):
#        return "Hello {}, Welcome".format(self.full_Name)

#    @staticmethod
#    def welcome_msg(Name):
#        return "Hello {}, Welcome".format(Name)

    @classmethod
    def welcome_msg(cls):
        return "Hello {}, Welcome".format(cls.full_Name)