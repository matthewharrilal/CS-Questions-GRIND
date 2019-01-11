def repeatedNTimes(A):

  """
  :type A: List[int]
  :rtype: int
  """
  lst_len = len(A)
  frequency_dict = {}
  
  for num in A:
    
    if num not in frequency_dict:
      frequency_dict[num] = 1
    else:

      frequency_dict[num] += 1
      if frequency_dict[num] == (lst_len / 2):
        return num
  return frequency_dict



def intersection(nums1, nums2):
  # FIND INTERSECTION OF ELEMENTS IN ARRAY
  """
  :type nums1: List[int]
  :type nums2: List[int]
  :rtype: List[int]
  """
  output = []
  
  for num_1 in nums1:
    for num_2 in nums2:
      if num_1 == num_2:
        if num_1 not in output:
          output.append(num_1)
  return output

 # REFACTORED
  '''
    d1 = {}
        d2 = {}
        for n1 in nums1:
            d1[n1] = 0
        
        for n2 in nums2:
            if n2 in d1:
                d2[n2] = 0
        
        return d2.keys()
  '''



 '''Definitely wouldn't have came up with this solution'''

 # HOWEVER IT MAKES SENSE WHEN YOU USE COUNT SORT YOU ARE USING IT WHEN YOU 
 #SORT INTEGERS AND YOU HAVE A LIMITED RANGE

  def sort_scores(scores, high):
    """sorts a list of scores. high is the highest possible"""

    print("")

    # variables:
    #    scores -- the array of items to be sorted;
    #    high -- a number such that all keys are in the range 0..high - 1
    #    count -- an array of numbers, with indexes 0..k-1, initially all zero
    #    n -- length of scores array
    #    sorted_scores -- an array of items, with indexes 0..n-1
    #    x -- an individual input item, used within the algorithm
    #    total, oldCount, i -- numbers used within the algorithm

    count = [0] * (high + 1)


    # calculate the histogram of scores:
    for x in scores:
        count[x] += 1
    # calculate the starting index for each key:


    total = 0
    for i in range(high + 1):   # i = 0, 1, ... k-1
        oldCount = count[i]
        count[i] = total # Number at index represents that its at that indexed seat in the sorted scores array

        total += oldCount
    print(count)



    # copy to output array, preserving order of scores with equal keys:
    sorted_scores = [0] * (len(scores))
    for x in scores:
        print(x)
        index = count[x] # Look at count array where x = the index
        sorted_scores[index] = x # When in the counted array its already sorted so the number at that frequency represents its seat in the sorted array 
        count[x] += 1 # If there is duplicates in the array then seat the next occurence of that number at seat number 3
        

    return sorted_scores


'''BETTER REFACTOR'''
def sort_scores(unsorted_scores, highest_possible_score):
    
    '''Why do we use count sort?
    
    We use it when we have to sort integers and we are given a limited range
    
    USEFUL TIP TO REMEMBER'''
    
    if len(unsorted_scores) == 0 or len(unsorted_scores) == 1:
        return unsorted_scores

    # Sort the scores in O(n) time
    count = {}
    for score in unsorted_scores:
        if score not in count:
            count[score] = 1
        else:
            count[score] += 1
    
    sorted_array = []
    for current_num in range(0, highest_possible_score + 1):
        # Meaning that we  have found score in sorted order 
        if current_num in count:
            sorted_array.extend([current_num] * count[current_num]) # Extend by the frequency of how many of those elements are there and you have those from the histogram
            
    return sorted_array


print(sort_scores([37, 89, 41, 65, 91, 53], 100))