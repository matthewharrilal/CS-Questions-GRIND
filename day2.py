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