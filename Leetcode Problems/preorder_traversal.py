class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # visit
        # left
        # right
        
        stack = []
        done = False
        output = []
        
        while not done:
            while root is not None:
                output.append(root.val) # Visit first
                stack.append(root)
                root = root.left
                
            if len(stack) == 0:
                return output
            
            current_node = stack.pop(len(stack) - 1)
            root = current_node.right
            
