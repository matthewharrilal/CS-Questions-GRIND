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

        parent_node = self.find_parent_node(item) # Going to pass by value ... still alters just a copy

        if item <= parent_node.data:
            parent_node.left = new_node
        
        else:
            parent_node.right = new_node
        
    
    def find_parent_node(self, item):
        '''Finds parent node of given item'''

        # Not checking for the case if BST doesn't contain the item at all ... assuming all nodes are valid for the meanwhile
        

        current_node, parent_node = self.root, None
        


        if current_node.data == item: 
            return None # No parent node of the root node

        while current_node is not None:

            if current_node.data == item:
                return parent_node

            if item <= current_node.data: # If item is smaller then root traverse left
                
                parent_node = current_node
                current_node = current_node.left
                print("Coming in here ", parent_node.data)

            else: # If item is bigger than root then traverse right
                parent_node = current_node
                current_node = current_node.right

        return parent_node # If doesnt find the exact item return leaf while the current node will be none

    def in_order_traversal(self):
        '''Returns a list of items contained inside the BST'''

        output = []
        current_node = self.root

        stack = []
        done = False

        while not done:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left

            if len(stack) == 0:
                return output
            
            current_node = stack.pop(len(stack) - 1)

            output.append(current_node.data)

            current_node = current_node.right

        # return output

# class ListNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.previous_pointer = None
#         self.next_pointer = None

# class DoublyLinkedList(object):
#     def __init__(self, bst_iterable=None):
#         self.head = None
#         self.size = 0
#         if bst_iterable is not None:
#             for 


items = [45, 23, 90, 15, 30, 60, 100]

tree = BinarySearchTree(items)

print(tree.in_order_traversal())