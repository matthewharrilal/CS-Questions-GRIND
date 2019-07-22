# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head # Your usual thangs with linked list nodes
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        
        
        current_node = self.head
        challenger_node = self.head.next
        
        
        counter = 0
        
        while challenger_node is not None:
            counter += 1
            
            # Keep the rate of probability consistent with the amount of nodes that you have traversed therefore the chance of choosing a random element stays consistent with the amount of work that you have done
            if random.randint(0, counter) == 0:
                current_node = challenger_node
            
            challenger_node = challenger_node.next
        
        return current_node.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()