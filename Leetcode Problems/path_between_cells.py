# Find a path between cells

# 1 -> Marks the source
# 2 -> Marks the destination
# 3 -> Marks a blank cell
# 4 -> Marks a blank wall

# Can only traverse through the blank cells

# Given the matrix [
# [0,3,2]
# [3,3,0]
# [1,3,0]
# ]  return true if there is a valid pathway from source to destination


def find_valid_pathway(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    source = None
    destination = None

    # The first task is to find the source point position and return the coordinates of that point 
    for row_index in range(rows):
        for column_index in range(columns):
            current_element = matrix[row_index][column_index]

            if current_element == 1:  # Meaning that we found the source
                source = (row_index,column_index)

            if current_element == 2:  # Meaning we found the destination
                destination = (row_index, column_index)

    
    # Now that we are able to retrieve the source point we have to traverse through our empty cells which are the (3)'s

    # Outline our base cases but what is the general solution ... we know how to navigate through our matrix through up down left and right

matrix = [[0,3,2], [3,3,0], [1,3,0]]
print(find_valid_pathway(matrix))