def findRestaurant(self, list1, list2):
        
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        # So whats the plan of action? First we have to see which restaurants they share, once doing so we then have to compare the sum of the indices they are presented at
        
        # My idea is to have a hash table store the indices of the first restaurant and compare to the second list if there is a collision check the sums but don't stop there use a current least to keep track of the least sum of indices
        
        restaurant_indices = {}
        least_sum = 1000000
        output = [None] * 1
        
        for index,res in enumerate(list1):
            restaurant_indices[res] = index
            
        for index, res in enumerate(list2):
            if res in restaurant_indices: # If there is a collision
                # least_sum = min(least_sum, (index + restaurant_indices[res])) # Compare it to the sum of the two indices
                
                if (index + restaurant_indices[res]) < least_sum:
                    least_sum = index + restaurant_indices[res]
                    output[0]  = res
                elif index + restaurant_indices[res] == least_sum:
                    output.append(res)
        return output