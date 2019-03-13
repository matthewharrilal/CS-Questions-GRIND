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

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.previous_pointer = None
        self.next_pointer = None

class DoublyLinkedList(object):
    def __init__(self, bst_tree=None):
        self.head = None
        self.size = 0
        if bst_tree is not None:
            self.convert(bst_tree) # Converts bst tree to doubly linked list

    def convert(self, bst_tree):
        sorted_data = bst_tree.in_order_traversal()
        print(sorted_data)

        previous_node = ListNode(sorted_data[0]) # Configure the first node

        previous_node.previous_pointer = None

        for index in range(1, len(sorted_data)):
            current_node = ListNode(sorted_data[index])
            previous_node.next_pointer = current_node
            current_node.previous_pointer = previous_node
            

            if previous_node.previous_pointer is None:
                print("Start")

            else:
                print(previous_node.previous_pointer.data, previous_node.data,  previous_node.next_pointer.data)

            previous_node = current_node
            
            # And then for the next iteration we have to make the previous node the current node

            

        current_node.next_pointer = None # Setting last pointer to non e

        return current_node


items = [3,2,4,1,5]

tree = BinarySearchTree(items)

doublyLinkedList = DoublyLinkedList(tree)

# print(tree.in_order_traversal())