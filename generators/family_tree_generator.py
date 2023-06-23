import random
import names
import sys

sys.path.append("..")
from entities.family import Family
from entities.family_member import FamilyMember
from entities.family_node import FamilyNode
from entities.family_tree import FamilyTree
from config.constants import *

class FamilyTreeGenerator:    
    @classmethod
    def generate_family_tree(cls, family: Family, generations: int):
        generation_count = 0
        family_tree = FamilyTree()
        max_generation_age = MAX_AGE_YEARS if generations == 1 else GENERATIONS_PACE_YEARS * generations
        min_generation_age = MIN_AGE_YEARS
        
        while generation_count <= generations:
            if generation_count == 0:
                first_generation_node = cls.generate_first_generation_node(cls, family, min_generation_age, max_generation_age)
                family_tree.set_root(first_generation_node)
            else:
                previous_generation_nodes = family_tree.get_nodes_at_level(generation_count-1)
                generations_left = generations - generation_count
                delta = cls.calculate_max_and_min_generation_age_pace(cls, generations, generations_left, min_generation_age, max_generation_age)
                max_generation_age -= delta
                min_generation_age -= delta

                for node in previous_generation_nodes:
                    children_count = random.randint(MIN_CHILDREN, MAX_CHILDREN)
                    cls.generate_couple_node(cls, node, random.randint(min_generation_age, max_generation_age))
                    for _ in range(0, children_count):
                        child_age = random.randint(min_generation_age, max_generation_age)
                        child = FamilyMember(node.male.family, child_age)
                        node.add_child(child)
            generation_count += 1

        return family_tree

    def generate_first_generation_node(self, family, min_generation_age, max_generation_age):
        male_age = random.randint(min_generation_age, max_generation_age)
        female_age = random.randint(min_generation_age, max_generation_age)
        female_family =  Family(names.get_last_name())

        male_partner = FamilyMember(family, male_age, gender='male')
        female_partner = FamilyMember(female_family, female_age, gender='female')

        male_partner.set_couple(female_partner)
        female_partner.set_couple(male_partner)

        return FamilyNode(female= female_partner, male= male_partner)
    
    def calculate_max_and_min_generation_age_pace(self, generations, generations_left, min_generation_age, max_generation_age):
        if min_generation_age < PARENTING_MIN_AGE:
            return 0
            
        difference_between_ages = max_generation_age - min_generation_age
        return difference_between_ages - random.randint(PARENTING_MIN_AGE, GENERATIONS_PACE_YEARS)
            
        
    def generate_couple_node(cls, node: FamilyNode, age: int):
        if node.female is not None and node.male is not None:
            return
        
        if node.female:
            family = Family(names.get_last_name())
            node.male = FamilyMember(family, age, gender='male')
            return

        if node.male:
            family = Family(names.get_last_name())
            node.female = FamilyMember(family, age, gender='female')
            return