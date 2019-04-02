# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorderTraversal(self, root):
        root_sequence = []
        stack = []
        done = False
        
        # Inorder traversal 
        while not done:
            while root is not None:
                
                # Add root to the stack for later processing
                stack.append(root)
                root = root.left
                
            # If there are no more nodes to traverse before we pop from the stack to process
            if len(stack) == 0:
                return root_sequence
            
            current_node = stack.pop(len(stack)  - 1)  # Pop the topmost element in the stack
            
            
            # We know that the left child is null and right is null we then hit a leaf node
            if current_node.right is None:
                
                root_sequence.append(current_node.val)
            
            root = current_node.right
        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        root1_sequence = self.inorderTraversal(root1)
        root2_sequence = self.inorderTraversal(root2)
        
        print(root1_sequence, root2_sequence)
        
        first_counter, second_counter = 0, 0 
        
        while first_counter < len(root1_sequence) and second_counter < len(root2_sequence):
            if root1_sequence[first_counter] != root2_sequence[second_counter]:
                return False
            
            first_counter += 1
            second_counter += 1
        return True