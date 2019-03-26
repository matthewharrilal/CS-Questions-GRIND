class Solution(object):
    
      # Size of graph is proportional to how many edges there are O(V + E) ~ O(E)
    
    def find(self, vertex, parent):
        if parent[vertex] == 0: # Meaning that we have found the representative element of the set
            return vertex # Following the path until we reach the representative element
        
        return self.find(parent[vertex], parent)  # Have to find the representative element of the parent element
        
    def union(self, first_set, second_set, parent):
        parent[first_set] = second_set  # Make the second element the representative element aka the parent element of the first element
        
        
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [0] * len(edges)
        
        for edge in edges:
            vertex_one, vertex_two = edge[0], edge[1]
            first_set, second_set = self.find(vertex_one - 1, parent), self.find(vertex_two - 1, parent)
            
            if first_set != second_set:
                self.union(first_set, second_set, parent)
                
            else:
                return [vertex_one, vertex_two]