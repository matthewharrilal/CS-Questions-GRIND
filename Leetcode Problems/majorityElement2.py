class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # We have to find the lower bound for how many times an element should appear
        lower_bound = math.ceil(len(nums) / 3)  # Has to be higher than or equal
        
        frequency_dict = {}
        output = []
        max_occurence = 1
        
        if len(nums) == 1:
            return [nums[0]]
        
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
                
            else:
                frequency_dict[num] += 1
                
            if frequency_dict[num] > max_occurence:
                output = [num] # Reset the array with the max element
                
                max_occurence = frequency_dict[num]  # Updates max_occurence counter
                
            elif frequency_dict[num] == max_occurence and frequency_dict[num] > lower_bound:
                output.append(num)
                
                    
        return output