def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        done = False # Flag determining if we have traversed all nodes, initially set to false
        
        stack = [] # To keep track of the nodes we have yet to look at
        
        while not done:
            
            while root is not None: # While there is a left subtree to traverse
                stack.append(root) # Going to be looking at this node in the future
                # k -= 1
                root = root.left
                
            # When we are done traversing the left subtree
            
            current_node = stack.pop(len(stack) - 1)
            k -= 1 # Only when you visit do you want to decrement k meaning that you reached the lowest number
            
            if k == 0:
                return current_node.val
            
            root = current_node.right