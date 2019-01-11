import unittest
import operator


def merge_ranges(meetings):

    # Merge meeting ranges
    
    meetings.sort(key = operator.itemgetter(0))
    output = [] # You have to sort it?
    output.append(meetings[0])
    
    for index in range(1, len(meetings)):
        previous_interval, current_interval = output[len(output) - 1], meetings[index]
        
        if previous_interval[1] >= current_interval[0]:
            previous_interval[1] = max(current_interval[1], previous_interval[1])
        else:
            output.append(current_interval)
    return output


import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    left, right = 0, len(list_of_chars) - 1
    
    while left <= right:
        temp = list_of_chars[left]
        list_of_chars[left], list_of_chars[right] = list_of_chars[right], temp
        left += 1
        right -= 1
        
    return list_of_chars
    





