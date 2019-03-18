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

# Keep track of the cumulative score of each person: if person a trusts person b, we decrement a's score and increment b's score.
# The judge is the only person that ends up with a score of N-1.

# I initialize the trusted list with N+1 items to make indexing easier, since the villagers are named 1 thorugh N.

# Time complexity O(N + T): T=len(trust). We iterate through the trust list once and through all villagers once, so the time complexity is linear in these. This is equivalent to |Vertices| + |Edges| in graph terms, if we consider each person as a vertex and each trust relationship as a directed edge.

# Space complexity O(N): We create a trusted list with a size of N+1 to store the cumulative scores.

def findJudge(self, N, trust):
	trusted = [0] * (N+1)
	for a, b in trust:
		trusted[a] -= 1
		trusted[b] += 1

	for i in range(1, N+1):
		if trusted[i] == N-1:
			return i
	return -1
