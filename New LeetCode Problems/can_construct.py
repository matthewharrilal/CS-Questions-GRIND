def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_freq = {}
        
        for letter in magazine:
            if letter not in letter_freq:
                letter_freq[letter] = 1
                
            else:
                letter_freq[letter] += 1
                
        for letter in ransomNote:
            if letter in letter_freq and letter_freq[letter] > 0:
                letter_freq[letter] -= 1
                
            else:
                return False
            
        return True