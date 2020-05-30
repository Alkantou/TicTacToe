# these two lines are to support type hints
from __future__ import annotations # this works only for python 3.7 and above
from typing import List


#This is an enum example . An enum is useful when we want to restrict the value of a string ( as an example )
from enum import Enum
class Sex(Enum):

    MALE = "M"
    FEMALE = "F"


class Person:

    # in the constructor below we pass a few <arg_name> : arg_type_hint(optional) = default_value(optional)
    # arg_type_hint is useful because it helps us describe what we expect that argument to be
    # default_value is useful because in this way we can pass nothing and a default value will be given
    def __init__(self, name : str = None  , sex : Sex = None, location : str = None, siblings : List[Person] = []):

        self.name = name
        self.sex = sex
        self.location = location
        self.siblings = siblings


    def speak(self):
        pass


    # exercise comment out and see before and after
    # def __repr__(self):
    #     return self.name+ " is a " + self.sex.value + " with " + str(len(self.siblings)) + " siblings : " + ",".join([x.name for x in self.siblings])





def history_of_the_world():
    # at the beggining
    k = Person(name="Kar", sex=Sex.MALE, location="Pat", siblings=[])

    # after
    a = Person(name="Al", sex=Sex.MALE, location="Pat", siblings=[k])
    k.siblings.append(a)

    # later
    e = Person(name="El", sex=Sex.FEMALE, location="Pat", siblings=[k, a])
    a.siblings.append(e)
    k.siblings.append(e)

    return {"The world now":{"People":[a,k,e]}}


print(history_of_the_world())













