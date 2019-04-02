# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        root1_sequence, root2_sequence = [], []
        stack = []
        done = False
        
        # Have to find a way to extract leaf sequence from binary tree
        
        
        # Inorder traversal 
        while not done:
            while root1 is not None:
                
                # Add root to the stack for later processing
                stack.append(root1)
                print(root1.val)
                root1 = root1.left
                
            # If there are no more nodes to traverse before we pop from the stack to process
            if len(stack) == 0:
                print("HERE ", root1_sequence)
                return root1_sequence
            
            current_node = stack.pop(len(stack)  - 1)  # Pop the topmost element in the stack
            
            
            # We know that the left child is null and right is null we then hit a leaf node
            if current_node.right is None:
                
                root1_sequence.append(current_node.val)
            
            root1 = current_node.right