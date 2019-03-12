# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def depthFirstSearch(self, root): # Result will return the smallest value in the tree ... aka the first time it visits
        done = False
        stack = []
        
        while not done:
            while root is not None:
                stack.append(root)
                
                root = root.left
                
            current_node = stack.pop(len(stack) - 1) # Lowest element ... first time we visit
            return current_node.val
        
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root.left is None and root.right is None:
            return - 1 # If the root node is only present
        
        if root.left:
            left_lowest = self.depthFirstSearch(root.left)
        else:
            left_lowest = -1
            
            
        if root.right:
            right_lowest = self.depthFirstSearch(root.right)
        else:
            right_lowest = -1
        
        if left_lowest == right_lowest:
            print("Special Case ", left_lowest, right_lowest)
            return -1
            
        return max(left_lowest, right_lowest)