class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        # First we have to create our adjacency matrix
        
        
        adj_matrix = [[0] * (N + 1)] * (N + 1) # Are all absent at first during instantiation
        counter = 0
        
        column = len(adj_matrix) # How many columns there are initially
        row = len(adj_matrix[0])
        
        print(adj_matrix)
        for column in range(column - 1):
            for row in range(row - 1):
                # print(adj_matrix[row])
                counter += 1
                
        return counter
        
#         if len(trust) == 0: # No townspeople
#             return -1
        
#         expected_judge = trust[0][1] # All townspeople have to be pointing to this judge
        
#         for towns_people in trust:
#             judge = towns_people[1]
#             if judge != expected_judge:
#                 return -1
            
#         return expected_judge

        