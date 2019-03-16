class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        frequency_dict = {}
        palindrome_count = 0
        
        for letter in s:
            if letter not in frequency_dict:
                frequency_dict[letter] = 1
                
            else: # If letter is contained inside the frequency dictionary
                frequency_dict[letter] += 1
                palindrome_count += frequency_dict[letter]
                frequency_dict.pop(letter) # Remove key value pair from dictionary
                
        if len(frequency_dict) > 0: # Only unique letters should be held in frequency dict after logic executes
            
               palindrome_count += 1
        
        return palindrome_count
        