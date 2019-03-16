# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        trackerHead = ListNode(0) # Used to keep reference to entire linked list
        previous = None
        
        if l1.val <= l2.val:
            previous = l1
            l1 = l1.next
            
        else:
            previous = l2
            l2 = l2.next
        
        trackerHead.next = previous # Once you have the head
        
        while l1 and l2:
            if l1.val <= l2.val:
                print("first node is greater ", l1.val)
                previous.next = l1
                l1 = l1.next
                
            else:
                print("Second node is greater at ", l2.val)
                previous.next = l2
                l2 = l2.next
                
            previous = previous.next
        
        
        remaining_node = l1 if l1 is not None else l2 # Only one of them will be none even at the same length
        print(remaining_node.next)
        while remaining_node is not None:
            previous.next = remaining_node
            remaining_node = remaining_node.next
            previous = previous.next
                
        return trackerHead.next