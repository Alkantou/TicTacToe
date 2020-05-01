class Person:

    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location


    def is_smart(self):
        return self.name[:4]!="Alex"


    def describe(self):
        return "Name : " + \
               self.name + \
               " Age : " + str(self.age) + \
               " location " + self.location + \
               " is smart : " + str(self.is_smart())
