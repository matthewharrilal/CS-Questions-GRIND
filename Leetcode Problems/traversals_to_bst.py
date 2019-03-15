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
        print("")
        print("ROOT ", root)
        
      
        
        # Locate root inside our inorder sequence to partition left and right subtrees
        
        inorder_root_index = inorder.index(root)
        
        # For the left
        if (inorder_root_index - start) == 0:
            
            print("Hit leaf at value ", root)
            root_position += 1
            return root_position
        
        # For the right
        if (end - inorder_root_index) == 0:
            
            # TODO : Set left child to none
            print("Hit leaf at value ", root)
            return
        
        
        # Find Left Subtree Values
        for index in range(start, inorder_root_index):
            left_value = inorder[index]
            print("LEFT SUBTREE VALUE ", left_value, root)
        
        # Then update root position so we know which element to look at next in preorder
        root_position = self.buildTree(preorder, inorder, start, inorder_root_index, root_position + 1)
        print("")
        
        # Find Right Subtree Values
        for index in range(inorder_root_index + 1, end  + 1):
            right_value = inorder[index]
            print("RIGHT SUBTREE VALUE ", right_value, root)
        
        self.buildTree(preorder, inorder, inorder_root_index + 1, end, root_position)
        
            
        