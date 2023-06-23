from .family_member import FamilyMember

class FamilyNode:
    def __init__(self, female: FamilyMember = None, male: FamilyMember = None, parent_node= None):
        
        if female is None and male is None:
            raise Exception('FamilyNode: both male and female are None. Empty nodes are not allowed')        

        self.female = female
        self.male = male
        self.children_nodes = []
        self.parent_node = parent_node
        self.children_count = 0

    def add_child(self, child: FamilyMember):
        child_node = FamilyNode(**{f"{child.gender}": child}, parent_node=self)
        self.children_nodes.append(child_node)
        self.children_count += 1

    def count_members(self, include_children=False):
        count = 0
        count += 1 if self.male else 0
        count += 1 if self.female else 0
        count += self.children_count if include_children else 0

        return count

    def get_family_name(self):
        if self.male and self.female:
            return f"{self.male.get_full_name()}-{self.female.get_full_name()}"
        elif self.male:
            return f"{self.male.get_full_name()}"
        else:
            return f"{self.female.get_full_name()}"

    def __repr__(self) -> str:        
        str = f"FamilyNode {self.get_family_name()}. They have {self.children_count} children. "

        for child in self.children_nodes:
            str += f"{child.female.get_full_name() if child.female else child.male.get_full_name()}, "

        return str
