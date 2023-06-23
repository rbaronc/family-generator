from .family_node import FamilyNode

class FamilyTree():
    def __init__(self, root: FamilyNode=None):
        self.root = root

    def set_root(self, root: FamilyNode):
        if root is None:
            raise Exception('FamilyTree: Root node cannot be None')
        else:
            self.root = root

    #root is at level 0
    def get_nodes_at_level(self, level: int):
        if level < 0:
            raise Exception('FamilyTree: Level must be greater than 0')

        if level == 0:
            return [self.root]
        else:
            nodes = []
            for child in self.root.children_nodes:
                nodes += self.get_nodes_at_level_recursive(1, level, child)

            return nodes
    
    def get_nodes_at_level_recursive(self, current_level, level, current_node: FamilyNode):
        if (current_level == level):
            return [ current_node ]
        else:
            nodes = []
            for child in current_node.children_nodes:
                nodes += self.get_nodes_at_level_recursive(current_level+1, level, child)

            return nodes
    
    def to_dict(self):
        tree_dict = {}
        self.to_dict_from_node([self.root], tree_dict)

        return tree_dict
    
    def to_dict_from_node(self, node_array, tree_dict):
        if len(node_array) == 0:
            return tree_dict
        
        node = node_array.pop(0)
        family_dict = {}
        
        if node.male:
            family_dict['male'] = f"{node.male.get_full_name()}-{node.male.age}"
        
        if node.female:
            family_dict['female'] = f"{node.female.get_full_name()}-{node.female.age}"
        
        if node.children_count:
            family_dict['children_count'] = node.children_count

        family_dict['children'] = {}
        for child in node.children_nodes:
            family_dict['children'][child.get_family_name()] = self.to_dict_from_node([child], {})

        tree_dict[node.get_family_name()] = family_dict

        return tree_dict
    
    def count_members(self):
        return self.count_members_from_node(self.root)
    
    def count_members_from_node(self, node):
        local_count = node.count_members()
        for child_node in node.children_nodes:
            local_count += self.count_members_from_node(child_node)
        return local_count