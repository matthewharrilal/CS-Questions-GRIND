def missingNumber(self, nums):
        
        # Get the sum of all numbers
        total_including_missing_number = ( len(nums) * ( len(nums) + 1 ) // 2 ) 
        
        return total_including_missing_number - sum(nums)