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