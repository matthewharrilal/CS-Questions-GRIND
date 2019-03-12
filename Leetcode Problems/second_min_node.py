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
        unique_values = set()
        
        while not done:
            while root is not None:
                print(root.val)
                stack.append(root)
                root = root.left
                
            if len(stack) == 0:
                return unique_values
                
            current_node = stack.pop(len(stack) - 1) # Doesn't gurantee lowest element not a binary search tree
            unique_values.add(current_node.val)
            
            root = current_node.right
            
        return unique_values
            
        
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        unique_values = self.depthFirstSearch(root)
        print("Unique Values", unique_values)
        
        removed_element = unique_values.remove(min(unique_values)) # If the set is empty after meaning there was no second smaller value
        
        if len(unique_values) == 0:
            return -1
        
        return min(unique_values)