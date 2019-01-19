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