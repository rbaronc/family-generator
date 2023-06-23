import names
import random
import sys

from .family_tree_generator import FamilyTreeGenerator

sys.path.append("..")
from entities.family import Family
from config import constants as CNFG


class FamiliyGenerator:
    @classmethod
    def generate_family(cls):
        family = Family(names.get_last_name())
        print(f"Generating family: {family.last_name}")
        generations = random.randint(CNFG.MIN_GENERATIONS, CNFG.MAX_GENERATIONS)
        family.family_tree = FamilyTreeGenerator.generate_family_tree(family, generations)

        return family

