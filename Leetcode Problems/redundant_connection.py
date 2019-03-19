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
        
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        adjacency_list = [[] for _ in range(len(edges) + 1)]
        
        for pair in edges:
            u, v = pair[0], pair[1]
            
            u_index = u - 1
            v_index = v - 1
            
            adjacency_list[u_index].append(v)
            
            adjacency_list[v_index].append(u)
            
            if len(adjacency_list[u_index]) > 1:
                for vertex in adjacency_list[u_index]:
                    if v in adjacency_list[vertex - 1]:
                        return [u, v]
                        
            
            
                
        return None
        