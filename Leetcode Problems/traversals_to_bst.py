# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        
        counter = 0
        
        root = preorder[counter] # Base root is the first element in our preorder sequence
        
        # Locate root inside our inorder sequence to partition left and right subtrees
        
        inorder_root_index = inorder.index(root)
        
        # Find Left Subtree Values
        for index in range(0, inorder_root_index):
            left_value = inorder[index]
            print("LEFT SUBTREE VALUE ", left_value)
        
        # Find Right Subtree Values
        
        for index in range(inorder_root_index + 1, len(inorder)):
            right_value = inorder[index]
            print("RIGHT SUBTREE VALUE ", right_value)