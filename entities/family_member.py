import names
import random
import functools

from .family import Family

class FamilyMember():
    def __init__(self, family: Family, age:int, gender=None):
        self.gender = gender if gender else self.generate_gender()
        self.first_name = names.get_first_name(gender=self.gender)
        self.family = family
        self.age = age
        self.state = self.generate_state()

    def generate_gender(self):
        return random.choice(['male', 'female'])
    
    def get_full_name(self):
        return f"{self.first_name} {self.family.last_name}"
    
    def generate_state(self):
        return random.choice(['Alive', 'Dead', 'Sick', 'Healthy'])
    
    def set_couple(self, couple):
        if couple is not None and isinstance(couple, FamilyMember):
            self.couple = couple
        else:
            raise Exception(f"The couple you're trying to set is not an instance of FamilyMember")

    def set_children(self, children):
        if len(children):
            if functools.reduce(lambda result, child: result and isinstance(child, FamilyMember), children):
                self.children = children
            else:
                raise Exception("Any/All of the children is not an instance of FamilyMember class")
        else:
            raise Exception(f"Cannot set children form {self.get_full_name} with an empty array")
        
    def add_child(self, child):
        if isinstance(child, FamilyMember):
            self.children.append(child)
        else:
            raise Exception("The child you are trying to add is not an instance of FamilyMember")
    
    def greet(self):
        return f"Hi, my name is {self.get_full_name()} and I'm a {self.gender}. I'm {self.age} years old. I'm currently {self.state}."