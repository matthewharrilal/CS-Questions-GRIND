# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ''' REVERSED ORDER TRAVERSAL ORDERING
        
            # left --> visit
            # right --> right
            # visit --> left
        '''
            
        unprocessed_nodes = []
        reversed_postorder = []
        output = []
        
        if root is not None:
            unprocessed_nodes.append(root) # Only becomes processed once node's left and right children have been added to be processed
            
        
        while len(unprocessed_nodes) > 0: # Meaning that there are still nodes to be worked on

            last_node_index = len(unprocessed_nodes) - 1
            current_node = unprocessed_nodes.pop(last_node_index) # Pop last node in

            # Current Node has been processed add its children to be processed next
            reversed_postorder.append(current_node.val)
            if current_node.left is not None:
                unprocessed_nodes.append(current_node.left)

            if current_node.right is not None:
                unprocessed_nodes.append(current_node.right)
                    
                
        
        for i in range( len(reversed_postorder) - 1, -1, -1) :
            current_val = reversed_postorder[i]
            output.append(current_val)
            
        return output
            