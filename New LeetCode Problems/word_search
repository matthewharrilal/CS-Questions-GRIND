class Solution(object):
    
#     def exist(self, board, word):
#         def search(board, x, y, word, visited=set()):
#             if word == '':
#                 return True
#             for i, j in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
#                 if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited and board[i][j] == word[0] and search(board, i, j, word[1:], visited | {(x, y)}):
#                     return True
#             return False
        
    
#         if not board or not board[0]:
#             return False
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0] and search(board, i, j, word[1:]):
#                     return True
#         return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # First step is calculating the neighbors inside the matrix
        rows = len(board)
        
        columns = len(board[0])


        # The only purpose of these for loops is to find the first element the recursive call handles the rest
        for row in range(rows):
            for column in range(columns):
                current_letter = board[row][column] 
                
                if current_letter == word[0] and self.dfs(board, row, column, word[1:], word):
                    return True
                    
                    
        return False
    
    def dfs(self, board, row, column, word, original_word,visited=None):
        if visited is None:
            visited = set()
        
        if word == "":
            print("In here")
            return True # Meaning that we found all letters until word was empty
            
        # Iterate through each of the neighbors for a given character
        for neighbor_row, neighbor_column in [(row, column - 1), (row, column + 1), (row + 1, column), (row - 1, column)]:
            
            # Checking three things if row/column is valid, if letter matches the letter we are looking for, and if we have been there already
            
            # IMPORTANT NOTE YOU HAVE TO USE THE PREVIOUS ROW AND COLUMN NOT UPDATED ITERATORS ... WHY b/c you haven't visited it if you are currently processing it
            if neighbor_row >= 0 and neighbor_row < len(board) and neighbor_column >= 0 and neighbor_column < len(board[0]) and board[neighbor_row][neighbor_column] == word[0] and (row, column) not in visited:
                print(row, column, word)
                
                if self.dfs(board, row, column, word[1:], original_word, visited | {(row, column)}):
                    return True
                
        print("Hitting here")
        return False

        
                    
                
        
            
            
class Solution(object):
    
#     def exist(self, board, word):
#         def search(board, x, y, word, visited=set()):
#             if word == '':
#                 return True
#             for i, j in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
#                 if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited and board[i][j] == word[0] and search(board, i, j, word[1:], visited | {(x, y)}):
#                     return True
#             return False
        
    
#         if not board or not board[0]:
#             return False
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0] and search(board, i, j, word[1:]):
#                     return True
#         return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # First step is calculating the neighbors inside the matrix
        rows = len(board)
        
        columns = len(board[0])


        # The only purpose of these for loops is to find the first element the recursive call handles the rest
        for row in range(rows):
            for column in range(columns):
                current_letter = board[row][column] 
                
                if current_letter == word[0] and self.dfs(board, row, column, word[1:], word):
                    return True
                    
                    
        return False
    
    def dfs(self, board, row, column, word, original_word,visited=None):
        if visited is None:
            visited = set()
        
        if word == "":
            print("In here")
            return True # Meaning that we found all letters until word was empty
            
        # Iterate through each of the neighbors for a given character
        for neighbor_row, neighbor_column in [(row, column - 1), (row, column + 1), (row + 1, column), (row - 1, column)]:
            
            # Checking three things if row/column is valid, if letter matches the letter we are looking for, and if we have been there already
            
            # IMPORTANT NOTE YOU HAVE TO USE THE PREVIOUS ROW AND COLUMN NOT UPDATED ITERATORS ... WHY b/c you haven't visited it if you are currently processing it
            if neighbor_row >= 0 and neighbor_row < len(board) and neighbor_column >= 0 and neighbor_column < len(board[0]) and board[neighbor_row][neighbor_column] == word[0] and (row, column) not in visited:
                print(row, column, word)
                
                if self.dfs(board, row, column, word[1:], original_word, visited | {(row, column)}):
                    return True
                
        print("Hitting here")
        return False

        
                    
                
        
            
            
