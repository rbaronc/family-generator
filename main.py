import random
import json

from config.constants import *
from generators.family_generator import FamiliyGenerator

def main():

    family_population = random.randint(FAMILY_MIN_POPULATION, FAMILY_MAX_POPULATION)    
    population_dict = generate_family_dict(family_population)

    with open('family.json', 'w') as outfile:
        population_serialized = json.dumps(population_dict, indent=4)
        outfile.write(population_serialized)
        print('Generated family.json')

    print(f"Total Population: {population_dict['population']}")


def generate_family_dict(family_population):
    family_dict = {}
    total_members = 0

    for _ in range(0, family_population):
        family = FamiliyGenerator.generate_family()        
        family_tree_dict = family.family_tree.to_dict()
        family_members_count = family.family_tree.count_members()        

        family_dict[family.last_name] = {
            'tree': family_tree_dict,
            'members': family_members_count
        }
        print(f"\tMembers: {family_members_count}")
        total_members += family_members_count
    
    family_dict['population'] = total_members

    return family_dict

if __name__ == '__main__':
    main()