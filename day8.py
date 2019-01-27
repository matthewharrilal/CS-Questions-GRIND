# DEDICATING TO SORTED ALGORITHMS

'''Selection sort what is the runtime and inefficiences you see with the sorting algorithm after you implement it'''

# [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
def selection_sort(unsorted_arr):
    counter = 0 # Marking the number of iterations we have to go through
    wall = 0 # Represents all sorted elements up to that wall

    for index in range(0, len(unsorted_arr)): # For every element compare it to the rest of the elements have to draw a grid to analyze run time
        wall = index
        for inner_index in range(index + 1, len(unsorted_arr)): # current element to all elements after the sorted pile
            compared_element = unsorted_arr[inner_index] # Represents the unsorted element we are comparing the current element to

            # If we find a new current minimum while comparing then update the current minimum
            if compared_element < unsorted_arr[wall]:                
                wall = inner_index
        # If or once we find the new current minimum we replace it with the element at the wall and start the next while loop iteration at wall + 1


        unsorted_arr[index], unsorted_arr[wall] = unsorted_arr[wall], unsorted_arr[index] # Make the swap and update wall for next while loop iteration

    return unsorted_arr

# def selection_sort(A):

#     for i in range(len(A)):

#         wall = i # Set the wall at the current element 
#         for compared_index in range(wall + 1, len(A)): # For the unsorted elements that occur after the wall just looking for a new minimum
#             print(compared_index,wall)
#             if A[compared_index] < A[wall]: # If the compared element we are on is bigger than the element at the wall we set the wall to be at that lower value index
#                 wall = compared_index # Setting the wall at the newly found minimum

#         # Swap the found minimum element with
#         # the first element
#         A[i], A[wall] = A[wall], A[i]
#         print(A)
#     return A


# print(selection_sort([29,10,14,37,14]))


# [29,10,14,37,14

def insertion_sort(unsorted_arr):
    for index in range(1, len(unsorted_arr)): # For every element compare to the element behind it
        current_num = unsorted_arr[index]
        backtracing_index = index - 1 # Marks the element previous
        
        while current_num < unsorted_arr[backtracing_index]: # while the current element is less than the elements before it
            unsorted_arr[backtracing_index + 1] = unsorted_arr[backtracing_index] 
            backtracing_index -= 1
        unsorted_arr[backtracing_index+1] = current_num 
    return unsorted_arr
    # It is only swapping pairs

print(insertion_sort([3,38,44,5,47,15,36,26,27,2,46,4,19,50,48]))
                