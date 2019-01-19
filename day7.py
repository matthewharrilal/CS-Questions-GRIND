def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # If we decrement in frequency then that is an intersection point
        
        num_set = set()
        output = []
        
        for num in nums1:
            num_set.add(num)
            
        for num in nums2:
            if num in num_set and num not in output:
                output.append(num)
                
        return output


def isValid(self, s):
        
        
        """
        :type s: str
        :rtype: bool
        """
        punc_openers = {"(": ")", "[":"]", "{": "}"}
        punc_closers = {")": "(", "]":"[", "}": "{"}
        opened_amount = 0

        punc_stack = []

        if s == "":
             return True
        if len(s) == 1:
            return False
        
        if s[0] not in punc_openers.keys(): # MEANING STRING STARTED OFF WITH CLOSED LETTER AUTOMATICALLY MAKING INVALID
              return False

        for index, letter in enumerate(s):
            if letter in punc_openers: # If letter is an opener then append it to the stack
                punc_stack.append(letter)
                opened_amount += 1

            elif letter in punc_closers and punc_stack: # If letter is a closer then check if can be resolved in stack

                if punc_closers[letter] == punc_stack[len(punc_stack) - 1]:
                    punc_stack.pop(len(punc_stack) - 1)
                    opened_amount -= 1

                else:
                    return False
            else:
                return False

        return (opened_amount == 0)