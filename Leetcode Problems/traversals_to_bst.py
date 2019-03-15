# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder, start=None, end=None, root_position=None):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if start is None and end is None and root_position is None:
            # Upper and lower bounds
            start = 0
            end = len(inorder) - 1
            root_position = 0
            
        root = preorder[root_position] # Base root is the first element in our preorder sequence
        print("ROOT ", root)
        
        # Locate root inside our inorder sequence to partition left and right subtrees
        
        root_index = inorder.index(root)
        
        if (root_index - start) < 1:
            print("Hit base case for the left")
            return 
        
        if (end - root_index) < 1:
            print("Hit base case for the right")
            return
        
        # Find Left Subtree Values
        for index in range(start, root_index):
            left_value = inorder[index]
            print("LEFT SUBTREE VALUE ", left_value)
            
        # Build left subtree first with lower and upper bound which we calculate from the next element in preorder
        self.buildTree(preorder, inorder, 0, root_index, root_position + 1)
        
        # Find Right Subtree Values
        for index in range(root_index + 1, end  + 1):
            right_value = inorder[index]
            print("RIGHT SUBTREE VALUE ", right_value)
            
        self.buildTree(preorder, inorder, root_index + 1, len(inorder) - 1, root_position + 1)
            