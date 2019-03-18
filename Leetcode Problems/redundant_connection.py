class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        adjacency_list = [[] for _ in range(len(edges) + 1)]
        
        for pair in edges:
            u, v = pair[0], pair[1]
            
            adjacency_list[u - 1].append(v)
            
            if len(adjacency_list[v - 1]) > 0:
                return [u,v]
            else:
                adjacency_list[v - 1].append(v)
                
        return None
        