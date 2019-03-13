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

        
        if self.root is None:
            self.root = BinaryTreeNode(item)
            return
        
    
    def find_parent_node(self, item):
        '''Finds parent node of given item'''
        current_node = self.root 

        if current_node.data == item: 
            return None # No parent node of the root node

        if cur

        

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
