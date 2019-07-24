class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # First check for the first occurence of an island ... then pass that to the DFS
        
        rows = len(grid)
        columns = len(grid[0])
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    # print("STARTING OVER")
                    perimeter = self.dfs(grid, row, column)
                    
                    return perimeter
        
        
    def dfs(self, grid, row,  column, visited=None, total_perimeter=None):
         
        if visited is None:
            visited = set()
            total_perimeter = 0
    
        if (row, column) in visited:
            return total_perimeter

        for neighbor_row, neighbor_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
            # print(row, column)
            if neighbor_row < 0 or neighbor_row >= len(grid) or neighbor_column < 0 or neighbor_column >= len(grid[0]):
                total_perimeter += 1
             
            elif grid[neighbor_row][neighbor_column] == 0:
                total_perimeter += 1

            
            elif grid[neighbor_row][neighbor_column] == 1:  
                visited.add((row, column))
                total_perimeter = self.dfs(grid, neighbor_row, neighbor_column, visited, total_perimeter)

        return total_perimeter




class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)
        columns = len(grid[0])
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    # print("STARTING OVER")
                    perimeter = self.dfs(grid, row, column)
                    
                    return perimeter
        
    def dfs(self, grid, row,  column, visited=None, total_perimeter=None):
         
        if visited is None:
            visited = set()
            total_perimeter = 0
            
        if (0 <= row < len(grid)) == False or (0 <= column < len(grid[0])) == False:
            total_perimeter += 1
            return total_perimeter
        
        if grid[row][column] == 0:
            total_perimeter += 1
            return total_perimeter
        
    
        if (row, column) in visited:
            return total_perimeter
        
        
        # if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and (row, column) not in visited and grid[row][column] == 1:
        visited.add((row, column))
        total_perimeter = self.dfs(grid, row + 1, column, visited, total_perimeter)
        total_perimeter = self.dfs(grid, row - 1, column, visited, total_perimeter)
        total_perimeter = self.dfs(grid, row, column + 1, visited, total_perimeter)
        total_perimeter = self.dfs(grid, row, column - 1, visited, total_perimeter)

#         for neighbor_row, neighbor_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
#             # print(row, column)
#             if neighbor_row < 0 or neighbor_row >= len(grid) or neighbor_column < 0 or neighbor_column >= len(grid[0]):
#                 total_perimeter += 1
             
#             elif grid[neighbor_row][neighbor_column] == 0:
#                 total_perimeter += 1

            
#             elif grid[neighbor_row][neighbor_column] == 1:  
#                 visited.add((row, column))
#                 total_perimeter = self.dfs(grid, neighbor_row, neighbor_column, visited, total_perimeter)



        return total_perimeter



 def bfs(self, image, row, column, newColor, initial_value):
        
        # Creating a set to keep track of the visited nodes
        visited = set()
        
        queue = []  # Used to keep track of the nodes that we are currently travering
        
        
        if image[row][column] is not None:
            queue.append((row, column))
            
            
        # While there are nodes still left to travers
        while len(queue) > 0:
            row, column = queue.pop(0)
            
            # With the current row and column enqueue its children 
            if (0 <= row + 1 < len(image)) and (0 <= column < len(image[0])) and (row + 1, column) not in visited and image[row + 1][column] == initial_value:
                queue.append((row + 1, column))
            
            if (0 <= row - 1 < len(image)) and (0 <= column < len(image[0])) and (row - 1, column) not in visited and image[row - 1][column] == initial_value:
                queue.append((row - 1, column))
            
            if (0 <= row  < len(image)) and (0 <= column + 1 < len(image[0])) and (row, column + 1) not in visited and image[row][column + 1] == initial_value:
                queue.append((row, column + 1))
            
            if (0 <= row < len(image)) and (0 <= column - 1 < len(image[0])) and (row, column - 1) not in visited and image[row][column - 1] == initial_value:
                queue.append((row, column - 1))
        
            visited.add((row, column))
            image[row][column] = newColor
            
        return image
        