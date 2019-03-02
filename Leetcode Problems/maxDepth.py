# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # This question is essentially asking for the height of the binary tree
        
        # Stop when the node we enter becomes null
        if root is None:
            return 0 
        
        # The second base case is if you reach a leaf node
        if root.left is None and root.right is None:
            return 1 # Meaning that we have reached a leaf node
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))