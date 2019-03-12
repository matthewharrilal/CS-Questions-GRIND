# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        queue_nodes = []
        
        if root is not None:
            queue_nodes.append(root)
            
        while len(queue_nodes) > 0: # While there are nodes left to traverse
            current_node = queue_nodes.pop(0) # Pop the first element
            print(current_node.val, current_node.left, current_node.right)
            
            if current_node.left is not None:
                
                if current_node.left.val > current_node.val: # If value doesnt satisfy ordering property
                    return False
                
                queue_nodes.append(current_node.left)
                
            if current_node.right is not None:
                
                if current_node.right.val < current_node.val: # If value doesn't satisfy ordering property
                    return False
                
                queue_nodes.append(current_node.right)
                
        return True