class Solution(object):
    def findCandidate(self, nums):
        majority_index = 0
        count = 1  # Set majority element to be the element at the first index and initial frequency of the element is 1
        
        for index in range(1, len(nums)):
            majority_element = nums[majority_index]
            element = nums[index]
            
            if majority_element == element:  # If the current element matches our majority element
                count += 1
                
            else:  # If the current element does not match our majority element
                count -= 1
                
            if count == 0:  # Update the majority index to be the current index
                majority_index = index
                count = 1  # Set the count back to 1 to represent the initial frequency
            
        return nums[majority_index]
        
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        frequency = len(nums) / 3
        counter = 0
        
        majority_element = self.findCandidate(nums)
        print(majority_element)
        
        for element in nums:
            if majority_element == element:
                counter += 1
                
        if counter > frequency:
            return [majority_element]
        
        else:
            return []
        