def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Order in this problem doesnt matter so its unique
        # Valid anagram if it has the same amount of letters and frequency
        
        frequency_dict = {}
        for letter in s:
            if letter not in frequency_dict:
                frequency_dict[letter] = 1
            else:
                frequency_dict[letter] += 1
        
        for letter in t:
            if letter in frequency_dict:
                frequency_dict[letter] -= 1
            else:
                return False
        for value in frequency_dict.values():
            if value != 0:
                return False
        return True

print(isAnagram("cat", "act"))