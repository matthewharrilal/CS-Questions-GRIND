def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_char = set()
        backtracing_index = 0
        
        # WHAT ARE THE MOST BASIC TRUTHS ABOUT THIS PROBLEM AWAY FROM CODING
        for index,letter in enumerate(s):
            if letter not in unique_char:
                unique_char.add(letter)
            else:
                # START NEW SEQUENCE bc you know repeating character right behind it not neccasarily true for example "bcdbg" # The sequence repeats at b but b isn't neccesarily behind it so we have to back track to the index of the previous time that element occured plus 1
                unique_char.clear
                backtracing_index = index
                while index != 0:
                    if s[backtracing_index] == letter:
                        # Found the previous occurence of the repeating letter have to add next letter to set and then start the loop from there so we need two while loops instead of one for loop and one while loop
                        
