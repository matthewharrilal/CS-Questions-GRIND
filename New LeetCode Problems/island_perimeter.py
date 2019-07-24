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