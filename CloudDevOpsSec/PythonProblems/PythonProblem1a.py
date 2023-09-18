class Person:

    def __init__(self, Name):
        self.full_Name = Name

    def welcome_msg(self):
        return "Hello {}, Welcome".format(self.full_Name)