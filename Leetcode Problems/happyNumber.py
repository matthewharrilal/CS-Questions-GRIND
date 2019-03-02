class Solution(object):
    def isHappy(self, n, nonRepeat=None):
        """
        :type n: int
        :rtype: bool
        """
        
        if nonRepeat is None:
            nonRepeat = set()
            
        counter = 0
        
        # Successful base case 
        print("N -> ", n)
        if n == 1:
            print("In here")
            return True
        
        for num in str(n):
            counter += pow(int(num), 2)
            
        if counter in nonRepeat:
            print(nonRepeat)
            return False # Detection of an infinite loop
            
        else:
            nonRepeat.add(counter)
        return self.isHappy(counter, nonRepeat)
            