class Solution(object):
    
    # A utility function to do union of two subsets 
    def union(self,parent,u,v): 
        u_set = self.findParentSubset(parent, u) 
        v_set = self.findParentSubset(parent, v) 
        parent[u_set] = v_set 
    
    def findParentSubset(self, parent, vertex):
        if parent[vertex] == -1: 
            return vertex
        
        if parent[vertex]!= -1: 
            # print("In here")
            return self.findParentSubset(parent,parent[vertex]) 
            
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        parent = [-1] * len(edges) # Single element sets no edges between vertices yet
        
        for pair in edges:
            u,v = pair[0], pair[1]
            
            # Need -1 of vertices because dealing with list indices
            u_subset = self.findParentSubset(parent, u - 1)
            v_subset = self.findParentSubset(parent, v - 1)
            
            # if u == 1:
            #     print("SUbset that 1 belongs to ", u_subset)
            
            # If elements lie in the same subset
            if u_subset == v_subset:
                return [u,v]
            
            else: # Create edge between two subsets
                self.union(parent, u - 1, v - 1)
        

            
            
        
        