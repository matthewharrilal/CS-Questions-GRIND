# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue_nodes = [] # Used to keep track of the traversal
        done = False # Stops under the condition that we have traversed all nodes
        output = [] # Picks up elements on the way
        
        
        if root is not None:
            output.append([root.val])
            queue_nodes.append(root) # Representing the initial level only containing the root
            
        
        while len(queue_nodes) > 0:
            current_node = queue_nodes.pop(0) # So we are appending the left and right child
            level = []
            
            if current_node is not None:
                                
                if current_node.left: # You know when you append children you are going to go a level deeper
                    
                    level.append(current_node.left.val)
                    queue_nodes.append(current_node.left)

                if current_node.right:
                    
                    level.append(current_node.right.val)
                    queue_nodes.append(current_node.right)
                    
                if level: # Meaning that there were valid nodes present on the level
                    output.append(level)
            
        return output