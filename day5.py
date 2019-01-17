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


def lemonadeChange(self, bills):

        # ADDINFG DYNAMICNESS TO FINAL SOLUTION SEEMS TO BE A BIT CHALLENGING DIFFERENT LOGIC INVOLVED REGARDING FINDING DIFFERENT VARIATIONS OF CHANGE THAT CAN BE GIVEN AND CHERCKED FOR
        
        """
        :type bills: List[int]
        :rtype: bool
        """

        # KEEPS TRACK OF HOW MANY 5'S AND 10'S YOU HAVE
        5_dollar_freq = 0
        10_dollar_freq = 0


        for i in range(len(bills)): # Iterate through given bills from customers

            if bills[i] == 5: # IF CUSTOMER GIVES YOU 5 COLLECT IT NO CHANGE GIVEN LEMONADE COST AT 5 DOLLARS CUSTOMERS ONLY BUY ONE
                5_dollar_freq += 1 # increment your five dollar frequency

            elif bills[i] == 10: # IF CUSTOMER GIVES YUO 10 DOLLARS
                if 1 > 5_dollar_freq: # IF YOU HAVE 1 OR MORE 5 DOLLAR BILLS

                    return False  # IF NOT RETURN FALSE BECAUSE WE HAVE NO CHANGE FOR HIM in the form they need
                else:
                    10_dollar_freq, 5_dollar_freq = 10_dollar_freq +1 , 5_dollar_freq -1 # INCREASE THE THE FREQUENCY OF THE BILL YOU COLLECTED(10) AND DECREMENT THE FREQUENCY OF THE BILL YOU GAVE AWAY(5)

            elif 10_dollar_freq > 0: # IF THE BILL IS NOT A 5 OR 10 ITS A 20 AND YOU KNOW THAT BECAUSE 20 IS THE ONLY OTHER BILL
                # THEREFORE CHECK THE FREQUENCY OF YOUR BIGGER BILLS FIRST BECAUSE YOU WANT TO GET RID OF THE BIGGER BILLS FIRST
                # THIS ELIF STATEMENT CONFIRMS TWO THINGS WE ARE CURRENTLY ON A 20 DOLLAR BILL AND THAT HAVE WE 1 OR MORE 10 DOLLAR BILLS

                if 5_dollar_freq >0: # CHECK FIRST IF YOU HAVE 5 DOLLAR BILLS
                    5_dollar_freq, 10_dollar_freq = 5_dollar_freq-1, 10_dollar_freq-1 # THEREFORE WE GIVE A 10 DOLLAR BILL AND A 5 DOLLAR BILL AWAY BY DECREMENTING IT AND THIS ACCOUNTS FOR ONE VARIATION OF POSSIBLE CHANGE GIVEN!!!!
                else:
                    return False

            else:
                if 5_dollar_freq < 3: # IF THE FIRST DESIRED VARIATION DOESNT WORK THEN SEE IF YOU CAN GIVE 3 FIVE DOLLARS AWAY 
                    return False
                else:
                    5_dollar_freq -= 3

        return True



# CLOSEST DYNAMICE ATTEMPT OF MINE AT LEMONADE CHANGE
def lemonadeChange(bills):
  """
  :type bills: List[int]
  :rtype: bool
  """

  # EVERYONE BUYS OONLY ONE LEMONADE

  bill_freq = {} # Frequency of the bills
  lemonade_price = 5 # Cost of 1 lemonade
  difference_left = 0
  
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
      elif profit not in bill_freq: # Either means we dont have correct change or that we need a variation of change

      # it all comes down to if we have the correct change 
        bill_freq[bill] = "NO CHANGE LEFT"

  # So whats the current situation we are able to collect the bills and hand out change and decrement when we do so. The problem now is though that we dont have a method to give a varaition of change for the highest bill =20$ next challenege think how to make the cap any factor of 5

  # If bill
   

  return bill_freq



  # How do we check for the different variations in bills that can be returned?

print(lemonadeChange([5,5,5,10,20]))



def findContentChildren(g, s):
  """
  :type g: List[int]
  :type s: List[int]
  :rtype: int
  """
  # LENGTH = NUMBER OF STUDENTS
  # ELEMENTS IN ARRAY REPRESENTS CURRENT STUDENTS GREED FACTOR
  # SECOND_ARR_LEN = NUMBER OF COOKIES
  # ELEMENTS IN SEC ARRAY = COOKIE SIZE
  # GREED FACTOR IS COMPLETED BY CONTENT ZISE
  
  # DO WE ACTUALLY CARE ABOUT THE STUDENT AS IN THEIR POSITION IN ARRAY JUST ABOUT THEIR GREED FACTOR
  
  greed_freq = {}
  content_students = 0
  
  for greed_factor in g:
      if greed_factor not in greed_freq:
          greed_freq[greed_factor] = 1
      else:
          greed_freq[greed_factor] += 1
          
  # WE NOW HAVE A GREED FACTOR FREQUENCY NOW WHAT WE NOW DECREMENT FROM THE FREQUENCY OF GREED AS WE ITERATE THROUGH COOKIE SIZES AND SEE WHO WE CAN MAKE CONTENT
  
  for cookie_size in s:
      if cookie_size in greed_freq:
          if greed_freq[cookie_size] > 0:
            content_students += 1
            greed_freq[cookie_size] -= 1
          
  return content_students

print(findContentChildren([1,2,2], [2,3]))


def findContentChildren( g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # WHAT WAS THE THOUGHT PROCESS BEHIND SORTING IT, LET US BOIL IT DOWN TO ITS MOST BASIC TRUTHS of this problem

        # WE NEED TO COMPARE EVERY COOKIE SIZE TO EVERY STUDENT TO SEE IF WE CAN MAKE THEM CONTENT. 
        #THIS BRUTE FORCE APPROACH WILL TAKE O(N^2) TIME BECAUSE FOR EVERY STUDENT YOU ARE CHECKING EVERY COOKIE SIZE

        # BUT WHAT IF THERE WAS A BETTER SYSTEM TO FIND CONTENT STUDENTS IN THE NUMBER OF COOKIES YOU HAVE TO CHECK BEFORE FINDING A MINIMUM COOKIE SIZE

        # SO THE NEXT THOUGHT THAT COMES INTO THINKING ABOUT THIS PROBLEM IS THAT YOU KNOW HAS A STUDENTS GREED FACTOR GETS LARGER THE COOKIE 
        # SIZE TO SATISFY THE STUDENT GETS LARGER THEREFORE IF YOU SORT BOTH OF THEM BECAUSE YOU KNOW HAS THE STUDENTS GREED FACTOR GROW YOU DONT NEED TO HAVE POINTERS IN THE ARRAY GOING FORWARDS AND BACK
        # AND ALSO THOSE COOKIES WOULD HAVE TO GO ANYWAY BECAUSE ONE COOKIE PER STUDENT I MEAN EVEN IF YOU IGNORED THE FACT THAT THEY GROW TOGETHER IF SORTED IF YOU DIDNT SORT THEM YOU WOULD HAVE TO START FROM THE BEGINNING OF THE ARRAY EVERYTIME TO SEE IF THERE IS A HIGH ENOUGH VALUE THAT SATISFYS THE CURRENT STUDENTS GREED LEVEL SO IF YOU SORT YOU AT LEAST KNOW THAT IF THE STUDENTS GREED FACTOR GROWS YOUR ONLY CHANCE IS TO ALSO LOOK FORWARD IN THE ARRAY THEREFOREE ONE POINTER
        g = sorted(g)
        s = sorted(s)
        gi, si = 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
                si += 1
            else:
                si += 1
        return gi

        '''SO WHAT ARE THE KEY TAKEAWAYS FROM THIS O(N LOG N) findContentChildren problem that as a student's 
        greed factor grows the minimum size of the cookie in order to satisfy them has to  grow therefore
        if you sort both arrs you can ensure that order. The benefit of ensuring this order is that you dont have to keep
        checking the whole array to find a cookie size to satisdy a greedier kid and vice versa'''

        # BOIL IT DOWN TO ITS MOST BASIC TRUTHS