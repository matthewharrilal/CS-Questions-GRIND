def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_char = set()
        backtracing_index =  # Set to current index and works backward when iterating
        current_index = 0
        done_rewinding = False # FLAG TO MARK WE FOUND PREVIOUS REPEATED ELEMENT
        counter = 0

        # # WHAT ARE THE MOST BASIC TRUTHS ABOUT THIS PROBLEM AWAY FROM CODING
        # for index,letter in enumerate(s):
        #     if letter not in unique_char:
        #         unique_char.add(letter)
        #     else:
        #         # START NEW SEQUENCE bc you know repeating character right behind it not neccasarily true for example "bcdbg" # The sequence repeats at b but b isn't neccesarily behind it so we have to back track to the index of the previous time that element occured plus 1
        #         unique_char.clear
        #         backtracing_index = index
        #         while index != 0:
        #             if s[backtracing_index] == letter:
        #                 # Found the previous occurence of the repeating letter have to add next letter to set and then start the loop from there so we need two while loops instead of one for loop and one while loop
                        
        while index <= len(s):
            current_letter = s[index]
            if current_letter not in unique_char:
                unique_char.add(current_letter)

            # Meaning we found a repeating element
            elif current_letter in unique_char: 
                print("SET: %s" %(unique_char))
                unique_char.clear() # CLEAR THE SET TO START NEW SEQUENCY
                while not done_rewinding:
                    backtracing_index = index
                    if s[backtracing_index] == letter:
                        index = backtracing_index # If you found the previous repeated element then start while loop on first unique character you see again
                    backtracing_index -= 1# Keep rewinding back
            index += 1
        

def lengthOfLongestSubstring(s):
  """
  :type s: str
  :rtype: int
  """
  unique_char = set()
  backtracing_index = 0  # Set to current index and works backward when iterating
  current_index = 0
  counter = 0
  max_sequence_length = 0
                  
  while current_index < len(s): # Need to iterate through the elements

      current_letter = s[current_index] # Find the current letter

      if current_letter not in unique_char: # Check if letter has been found in the sequence

          unique_char.add(current_letter) # If not then add the letter to increase the sequence
          counter += 1 # Keeping track of sequence length

      # Meaning we found a repeating element
      else: 

          if counter > max_sequence_length:
            max_sequence_length = counter

          unique_char.clear() # Clear the sequence held in the set because we found a duplicate

          counter = 0 # Reset the counter to keep track of the length of the next sequence

          backtracing_index = current_index # Set the index to iterate back to find the previous occurence of the repeated element, why?

          while backtracing_index >= 0: # keeping track of when we are done backtracing to find the previous occurence of the last repeated element

            backtracing_index -= 1 # Backtrace
            if s[backtracing_index] == current_letter: # Check if the letter we are currently on while backtracing is the repeated element we encountered

              current_index = backtracing_index # Then set the current index to be the index after the previous occurence of the repeated element
              break

      current_index += 1 # Incremented here for the next iteration

  return max_sequence_length

    
print(lengthOfLongestSubstring("pwwkew"))




def minAddToMakeValid(S):
    """
    :type S: str
    :rtype: int
    """
    missing_counter = 0
    parenthesis_freq = {}
    opened = "("
    closed = ")"

    for index, parenthesis in enumerate(S):
      if parenthesis not in parenthesis_freq:
        parenthesis_freq[parenthesis] = [1, index]
      # else:
      #   parenthesis_freq[parenthesis] = parenthesis_freq[parenthesis][0] += 1

    # for parenthesis in S:

    #   # Resolve with closed parenthesis
    #   if parenthesis == opened: 
    #     if parenthesis_freq[closed] > 0:
    #       parenthesis_freq[closed] -= 1

    #     else:
    #       missing_counter += 1

    #   elif parenthesis == closed:
    #     if parenthesis_freq[opened] > 0:
    #       parenthesis_freq[opened] -= 1

    #     else:
    #       missing_counter += 1

    return parenthesis_freq


print(minAddToMakeValid("()))(("))