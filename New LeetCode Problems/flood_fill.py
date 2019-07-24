class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        initial_value = image[sr][sc]
        
        image = self.dfs(image, sr, sc, newColor, initial_value)
        
        return image
       
    
    
    def dfs(self, image, row, column, newColor, initial_value, visited=None):
        
        if visited is None:
            visited = set()
        
        if (row,column) in visited:
            return image
        
        
        
        # You only use a for loop for depth first search if you want to explore different paths from a given starting point
        if (0 <= row < len(image)) and (0 <= column < len(image[0])) and image[row][column] == initial_value and (row, column) not in visited:
            visited.add((row, column))
            image[row][column] = newColor
            
            image = self.dfs(image, row + 1, column, newColor, initial_value, visited)
            image = self.dfs(image, row - 1, column, newColor, initial_value, visited)
            image = self.dfs(image, row, column + 1, newColor, initial_value, visited)
            image = self.dfs(image, row, column - 1, newColor, initial_value, visited)
            
        
#         # For each of the row and columns for neighbors
#         for neighbor_row, neighbor_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1) ]:
            
#             print(row, column)
#             # First check if they are in bounds ... if they are in bounds then you check for color
            
#             if (0 <= neighbor_row < len(image)) and (0 <= neighbor_column < len(image[0])) and (row, column) not in visited:
                
                
                
#                 # If the current neighbor has the same color as the current pixel update
#                 if image[neighbor_row][neighbor_column] == initial_value:
                   
                    
#                     # First update the neighbor's color
#                     # image[neighbor_row][neighbor_column] = newColor
                    
#                     image[row][column] = newColor
                    
#                     visited.add((row,column))
                    
#                     self.dfs(image, neighbor_row, neighbor_column, newColor, initial_value, visited)
                    
#                     # After it's neighbors have been resolved change the centerpiece's color
                    
         
                    
        return image