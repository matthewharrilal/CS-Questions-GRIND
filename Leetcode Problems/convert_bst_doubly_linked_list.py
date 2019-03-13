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

        self.head = ListNode(sorted_data[0]) # Configure the first node

        previous_node = self.head

        previous_node.previous_pointer = None

        for index in range(1, len(sorted_data)):
            current_node = ListNode(sorted_data[index])
            previous_node.next_pointer = current_node
            current_node.previous_pointer = previous_node
            

            # if previous_node.previous_pointer is None:
                # print("Start")

            # else:
            #     # print(previous_node.previous_pointer.data, previous_node.data,  previous_node.next_pointer.data)

            previous_node = current_node
            
            # And then for the next iteration we have to make the previous node the current node

            

        current_node.next_pointer = None # Setting last pointer to non e

        return self.head


def merge_doublies(first_root, second_root):
    resulting_list = DoublyLinkedList()
    previous_node = None
    remaining_root = None

    # Initial configuration of resulting lists head
    if first_root.data <= second_root.data:
        resulting_list.head = ListNode(first_root.data)
        first_root = first_root.next_pointer # bump the first node

    else:
        resulting_list.head = ListNode(second_root.data)
        second_root = second_root.next_pointer # bump the second node

    # After this the head has been established make a copy and work with it

    current_node = resulting_list.head
    current_node.previous_pointer = previous_node
    
    while first_root is not None and second_root is not None:

        if first_root.data <= second_root.data:
            previous_node = first_root # Set previous node before we bump first counter
            current_node.next_pointer = first_root
            first_root = first_root.next_pointer

        else:
            previous_node = second_root
            current_node.next_pointer = second_root
            second_root = second_root.next_pointer

        if current_node.previous_pointer is None:
            print("Start")

        else:
            print(current_node.previous_pointer.data, current_node.data,  current_node.next_pointer.data)
        
        current_node = current_node.next_pointer

    
    remaining_root = first_root if first_root is not None else second_root

    if remaining_root is not None:
        while remaining_root is not None:
            current_node.next_pointer = remaining_root

            remaining_root = remaining_root.next_pointer

    
    return resulting_list

def printItems(resulting_list):
    current_node = resulting_list.head

    while current_node is not None:
        print(current_node.data)

        current_node = current_node.next_pointer




items = [7, 5, 2 , 9 , 12]

second_items = [3, 10, 8, 11]


tree = BinarySearchTree(items)

second_tree = BinarySearchTree(second_items)

doublyLinkedList = DoublyLinkedList()

second_list = DoublyLinkedList()

first_root, second_root = doublyLinkedList.convert(tree), second_list.convert(second_tree)

resulting_list = merge_doublies(first_root, second_root)

