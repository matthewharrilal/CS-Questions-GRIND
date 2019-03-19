"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        queue = [] # Track of neighbors that we have yet to visit
        visited = [False] # Can use vertex value as index
        done = False
        
        queue.append(node) # Root initially has no siblings
        
        while not done:
            if len(queue) == 0:
                return node # Return starting vertex # No more nodes to traverse
            
            current_vertex = queue.pop(0) # Remove the first element
            print(current_vertex.val)
            
            for neighbor in current_vertex.neighbors:
                vertex_in_visited = neighbor.val - 1
                
                
                while len(visited) < neighbor.val:
                    print(len(visited), neighbor.val)
                    visited.append(False)
                    
                if visited[vertex_in_visited] == False:
                    if neighbor not in queue:
                        queue.append(neighbor)
            visited[current_vertex.val - 1] = True

            