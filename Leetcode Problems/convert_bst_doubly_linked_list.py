class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self, items=None):
        self.root = None
        if items is not None:
            for item in items:
                self.insert(item) # Insert node into the given binary search tree
    
    def insert(self, item):

        new_node = BinaryTreeNode(item)
        
        if self.root is None:
            self.root = BinaryTreeNode(item)
            return

        parent_node = self.find_parent_node(item): # Going to pass by value ... still alters just a copy

        if item <= parent_node.data:
            parent_node.left = new_node
        
        else:
            parent_node.right = new_node
        
    
    def find_parent_node(self, item):
        '''Finds parent node of given item'''
        current_node, parent_node = self.root, None

        if current_node.data == item: 
            return None # No parent node of the root node

        while current_node is not None:


            if item <= current_node.data: # If item is smaller then root traverse left
                parent_node = current_node
                current_node = current_node.left

            else: # If item is bigger than root then traverse right
                current_node = current_node.right

            if current_node.data == item:
                return parent_node

        # Not checking for the case if BST doesn't contain the item at all ... assuming all nodes are valid for the meanwhile
        

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.previous_pointer = None
        self.next_pointer = None

class DoublyLinkedList(object):
    def __init__(self, bst_iterable=None):
        self.head = None
        self.size = 0
        if bst_iterable is not None:
            for 
