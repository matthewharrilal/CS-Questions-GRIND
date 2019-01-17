def largest_sum_consecutive_array(arr):
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum += num # Keep incrementing current_sum

        if current_sum < 0: # Meaning that the current sum has gone negative meaning starting at the next positive number will result in a bigger sum as a starting point
             current_sum = 0
        else:
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


print(largest_sum_consecutive_array([-2, -3, 4, -1, -2, 1, 5, -3]))


import collections
def findTheDifference(s, t):
  """
  :type s: str
  :type t: str
  :rtype: str
  """
  ss = collections.Counter(s)
  tt = collections.Counter(t)
  print(tt,ss)
  res = tt-ss
  return res.keys()[0]
print(findTheDifference(s = "abcd",t = "abcde"))


def lemonadeChange(bills):
  """
  :type bills: List[int]
  :rtype: bool
  """

  # EVERYONE BUYS OONLY ONE LEMONADE

  # ({10: 2, 20: 1, 5: 2}, [5, 5, 10, 10, 20])

  # DO WE EVEN CARE ABOUT PROFIT JUUST THE BILLS WE ARE COLLECTING

  # Decrement profit from freq and increment bill freq

  bill_freq = {} # Frequency of the bills
  lemonade_price = 5 # Cost of 1 lemonade
  
  for bill in bills:
    profit = (bill - lemonade_price)
    if lemonade_price == bill:
      if bill not in bill_freq:

        bill_freq[bill] = 1

      else:
        bill_freq[bill] += 1
    
    else:
      if bill in bill_freq:
        bill_freq[bill] += 1
      else:
        bill_freq[bill] = 1
      # PROFIT == BILL WE ARE DECREMENTING FREQ FROM
      if profit in bill_freq:
        bill_freq[profit] -= 1
      else:
        bill_freq[bill] = "NO CHANGE LEFT"

  return bill_freq



  # How do we check for the different variations in bills that can be returned?

print(lemonadeChange([5,5,5,10,20]))